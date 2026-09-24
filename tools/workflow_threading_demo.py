#!/usr/bin/env python3
"""Small standard-library demo of seed/vacate/propagate/return workflow threading.

Prototype only. It models temporal coordination state; it does not schedule real workers.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field, asdict
from datetime import datetime, timedelta, timezone
from typing import Dict, List, Optional, Set


@dataclass
class Seed:
    artifact: str
    version: str
    author: str
    consumers: List[str]
    policy: str = "optional-diversified"
    output_target: str = "THREAD_OUTPUTS/"
    exposure_policy: str = "record"


@dataclass
class ReturnCondition:
    min_outputs: int = 1
    min_workers: int = 1
    max_hours: float = 1.0
    require_success_and_failure: bool = False


@dataclass
class OutputReceipt:
    worker: str
    artifact: str
    seed_version: str
    outcome: str  # success | failure | mixed | blocker
    timestamp: str
    metadata: Dict[str, str] = field(default_factory=dict)


@dataclass
class ThreadState:
    thread_id: str
    parent_goal: str
    seed: Seed
    return_condition: ReturnCondition
    author_state: str = "active"  # active | vacated | rejoin-ready | rejoined | blocked
    status: str = "seeded"        # seeded | propagating | rejoin-ready | complete | blocked
    vacate_started_at: Optional[str] = None
    receipts: List[OutputReceipt] = field(default_factory=list)
    displaced_work: Optional[str] = None
    fallback: str = "reinsert author at time cap and reassess"
    return_action: str = "synthesize"

    def vacate(self, now: datetime) -> None:
        self.author_state = "vacated"
        self.status = "propagating"
        self.vacate_started_at = now.isoformat()

    def add_receipt(self, receipt: OutputReceipt) -> None:
        if receipt.seed_version != self.seed.version:
            raise ValueError("receipt seed version mismatch")
        self.receipts.append(receipt)

    @property
    def distinct_workers(self) -> Set[str]:
        return {r.worker for r in self.receipts}

    def elapsed_hours(self, now: datetime) -> float:
        if not self.vacate_started_at:
            return 0.0
        start = datetime.fromisoformat(self.vacate_started_at)
        return (now - start).total_seconds() / 3600.0

    def state_threshold_met(self) -> bool:
        c = self.return_condition
        if len(self.receipts) < c.min_outputs:
            return False
        if len(self.distinct_workers) < c.min_workers:
            return False
        if c.require_success_and_failure:
            outcomes = {r.outcome for r in self.receipts}
            if "success" not in outcomes or "failure" not in outcomes:
                return False
        return True

    def should_rejoin(self, now: datetime) -> Dict[str, object]:
        state_ready = self.state_threshold_met()
        time_ready = self.elapsed_hours(now) >= self.return_condition.max_hours
        ready = state_ready or time_ready
        reason = "state-threshold" if state_ready else ("time-cap" if time_ready else "not-yet")
        return {
            "ready": ready,
            "reason": reason,
            "outputs": len(self.receipts),
            "workers": len(self.distinct_workers),
            "elapsed_hours": round(self.elapsed_hours(now), 3),
        }

    def mark_rejoin_if_ready(self, now: datetime) -> Dict[str, object]:
        result = self.should_rejoin(now)
        if result["ready"]:
            self.author_state = "rejoin-ready"
            self.status = "rejoin-ready"
        return result


def sample_thread(now: Optional[datetime] = None) -> ThreadState:
    now = now or datetime.now(timezone.utc)
    thread = ThreadState(
        thread_id="thread-demo-001",
        parent_goal="Generate diverse evidence before the seed author returns to synthesize.",
        seed=Seed(
            artifact="tools/example_geometry_check.py",
            version="demo-v1",
            author="Meridian",
            consumers=["Mercer", "Orson", "Comptroller", "Aster"],
            policy="optional-diversified",
            output_target="WORKSPACES/COMMON/THREAD_OUTPUTS/thread-demo-001/",
        ),
        return_condition=ReturnCondition(
            min_outputs=4,
            min_workers=3,
            max_hours=3.0,
            require_success_and_failure=True,
        ),
        displaced_work="Meridian ordinary solver loop preserved for later restoration/rejoin.",
        return_action="compare outputs, revise helper, salvage failure cases, update candidate education",
    )
    thread.vacate(now)
    return thread


def run_demo() -> Dict[str, object]:
    t0 = datetime(2026, 9, 24, 17, 0, tzinfo=timezone.utc)
    thread = sample_thread(t0)

    snapshots = [{"label": "seeded-and-vacated", "state": asdict(thread), "gate": thread.should_rejoin(t0)}]

    receipts = [
        OutputReceipt("Mercer", "case-001.json", "demo-v1", "success", (t0 + timedelta(minutes=20)).isoformat(), {"method": "reproducibility"}),
        OutputReceipt("Orson", "case-002.json", "demo-v1", "failure", (t0 + timedelta(minutes=35)).isoformat(), {"method": "behavior-observation"}),
        OutputReceipt("Comptroller", "case-003.json", "demo-v1", "success", (t0 + timedelta(minutes=50)).isoformat(), {"method": "coverage"}),
    ]
    for r in receipts:
        thread.add_receipt(r)
    snapshots.append({"label": "three-receipts", "state": asdict(thread), "gate": thread.mark_rejoin_if_ready(t0 + timedelta(hours=1))})

    thread.add_receipt(OutputReceipt("Aster", "case-004.json", "demo-v1", "success", (t0 + timedelta(hours=1, minutes=10)).isoformat(), {"method": "alternate-input"}))
    snapshots.append({"label": "threshold-met", "state": asdict(thread), "gate": thread.mark_rejoin_if_ready(t0 + timedelta(hours=1, minutes=15))})

    return {"demo": snapshots}


def self_test() -> Dict[str, object]:
    t0 = datetime(2026, 9, 24, 17, 0, tzinfo=timezone.utc)

    thread = sample_thread(t0)
    assert thread.author_state == "vacated"
    assert thread.status == "propagating"

    thread.add_receipt(OutputReceipt("Mercer", "a", "demo-v1", "success", t0.isoformat()))
    assert not thread.should_rejoin(t0 + timedelta(minutes=30))["ready"]

    for i in range(3):
        thread.add_receipt(OutputReceipt("Mercer", f"same-{i}", "demo-v1", "failure" if i == 0 else "success", t0.isoformat()))
    assert len(thread.receipts) >= thread.return_condition.min_outputs
    assert len(thread.distinct_workers) == 1
    assert not thread.should_rejoin(t0 + timedelta(hours=1))["ready"]

    try:
        thread.add_receipt(OutputReceipt("Orson", "bad", "demo-v0", "failure", t0.isoformat()))
        raise AssertionError("version mismatch not rejected")
    except ValueError:
        pass

    thread2 = sample_thread(t0)
    thread2.add_receipt(OutputReceipt("Mercer", "a", "demo-v1", "success", t0.isoformat()))
    thread2.add_receipt(OutputReceipt("Orson", "b", "demo-v1", "failure", t0.isoformat()))
    thread2.add_receipt(OutputReceipt("Comptroller", "c", "demo-v1", "success", t0.isoformat()))
    thread2.add_receipt(OutputReceipt("Aster", "d", "demo-v1", "success", t0.isoformat()))
    gate = thread2.mark_rejoin_if_ready(t0 + timedelta(hours=1))
    assert gate["ready"] and gate["reason"] == "state-threshold"
    assert thread2.author_state == "rejoin-ready"

    thread3 = sample_thread(t0)
    gate = thread3.mark_rejoin_if_ready(t0 + timedelta(hours=3, minutes=1))
    assert gate["ready"] and gate["reason"] == "time-cap"

    return {"tests": 6, "status": "PASS"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["demo", "self-test", "schema"])
    args = parser.parse_args()

    if args.command == "demo":
        print(json.dumps(run_demo(), indent=2))
    elif args.command == "self-test":
        print(json.dumps(self_test(), indent=2))
    else:
        print(json.dumps(asdict(sample_thread(datetime.now(timezone.utc))), indent=2))


if __name__ == "__main__":
    main()
