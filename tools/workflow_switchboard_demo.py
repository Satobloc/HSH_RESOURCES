#!/usr/bin/env python3
"""Top/Central/Branch/Hydra switchboard proof-of-concept.

Standard-library only. This is a deterministic planner/state transformer, not a scheduler,
not a theory engine, and not a production workflow. It demonstrates wake/check routing,
actor+locale overlays, branch fan-out, sticky experience, and guarded recurrence rewrites.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from dataclasses import dataclass, asdict
from typing import Any

TOP = {
    "mutation": "locked",
    "rules": [
        "sandboxed theory is not promoted by workflow state",
        "provenance/exposure boundaries survive routing",
        "Nathan instructions guide behavior but are not automatically public content",
        "locked rules are not silently rewritten from observed model behavior",
        "current/ambiguous referents trigger bounded disconfirmation before nearest-memory capture",
    ],
}

SOURCES = {
    "dashboard_plans": {"kinds": {"planning", "priority"}},
    "hsh_common": {"kinds": {"control", "task", "handoff"}},
    "war_room": {"kinds": {"directive", "notice"}},
    "archive": {"kinds": {"history", "provenance", "conversation"}},
    "preference_runtime": {"kinds": {"preference", "behavior"}},
    "instance_workspaces": {"kinds": {"identity", "continuity", "experience"}},
    "capability_directory": {"kinds": {"tool", "plugin", "skill", "capability"}},
}

ACTORS = {
    "Comptroller": {
        "workspace": "HsH/WORKSPACES/COMMON",
        "rules": ["coverage before duplication", "repair routing gaps", "preserve displaced function"],
    },
    "Orson Vey": {
        "workspace": "HSH_RESOURCES/Consciousness + AI/VEY_COGNITION_LAB",
        "rules": ["behavior before self-report", "separate model/context/tool/workflow", "track exposure/false independence"],
    },
    "Meridian": {
        "workspace": "HsH/WORKSPACES/MERIDIAN",
        "rules": ["object type before equations", "prefer reconstructible solver geometry"],
    },
    "Sable": {
        "workspace": "HsH/WORKSPACES/SABLE",
        "rules": ["continuity/system coherence", "preserve distinct identities"],
    },
}

LOCALES = {
    "theory_workbench": {
        "requires": {"repo_read"},
        "rules": ["declare object/domain", "definition != assumption != consequence", "failed branches remain information", "promotion needs gate"],
        "override": True,
        "actor": {},
    },
    "math_toolbox": {
        "requires": {"python"},
        "rules": ["namespaced variables", "deterministic inputs where feasible", "record invariants/failures"],
        "override": True,
        "actor": {
            "Comptroller": ["toolbox=QA/coverage instrument", "tie output to exit criterion"],
            "Orson Vey": ["tool use is a workflow condition", "watch automation-created evidence/convergence"],
        },
    },
    "epistemic_locker": {
        "requires": set(),
        "rules": ["no unmarked assumption promotion", "counterexample lane mandatory", "claims carry evidence class"],
        "override": True,
        "actor": {},
    },
    "playground": {
        "requires": set(),
        "rules": ["wild generation allowed", "no egress without re-entry audit", "record useful wreckage"],
        "override": True,
        "actor": {},
    },
    "paper_shop": {
        "requires": {"repo_read"},
        "rules": ["claim/source alignment", "reader-facing terminology", "sandbox until release gate"],
        "override": False,
        "actor": {},
    },
}

BRANCHES = {
    "directive_intake": {"tags": {"directive", "current", "notice"}, "relation": "serial", "share": True},
    "capability_scout": {"tags": {"blocked", "capability", "tool", "plugin"}, "relation": "parallel", "share": True},
    "construct": {"tags": {"construct"}, "relation": "serial", "share": True},
    "math_check": {"tags": {"math", "theory_candidate"}, "relation": "perpendicular", "share": False},
    "adversarial_audit": {"tags": {"audit", "theory_candidate"}, "relation": "perpendicular", "share": False},
    "provenance_prior_art": {"tags": {"provenance", "theory_candidate"}, "relation": "perpendicular", "share": False},
    "prediction_packet": {"tags": {"prediction"}, "relation": "gated", "share": True},
    "paper_pipeline": {"tags": {"paper", "public_ready"}, "relation": "gated", "share": True},
    "prune_rebuild": {"tags": {"failed_check", "prune"}, "relation": "serial", "share": True},
    "continuity_education": {"tags": {"learning", "continuity"}, "relation": "parallel", "share": True},
}

HYDRA_NODES = [
    {
        "id": "fresh_directive_bootstrap",
        "when": {"fresh_directive": True},
        "spawn": [
            {"job": "extract_directive", "relation": "serial"},
            {"job": "map_control_impact", "relation": "parallel"},
            {"job": "test_worker_discovery", "relation": "perpendicular", "share": False},
        ],
        "rewrite": ("recurrence:freshness_watch", "watch unresolved incorporation + new deltas; retire when incorporated"),
    },
    {
        "id": "candidate_checks",
        "when": {"candidate_stage": "constructed", "event_tag": "theory_candidate"},
        "spawn": [
            {"job": "math_check", "relation": "perpendicular", "share": False},
            {"job": "adversarial_audit", "relation": "perpendicular", "share": False},
            {"job": "provenance_prior_art", "relation": "perpendicular", "share": False},
        ],
        "rewrite": ("recurrence:candidate_followup", "merge frozen checks: fail=>prune/rebuild; pass=>prediction+paper"),
    },
    {
        "id": "candidate_pass",
        "when": {"candidate_stage": "checked_pass"},
        "spawn": [
            {"job": "prediction_packet", "relation": "parallel"},
            {"job": "paper_pipeline", "relation": "parallel"},
            {"job": "independent_reality_check", "relation": "perpendicular", "share": False},
        ],
        "rewrite": ("recurrence:publication_readiness", "check claim/source/render/review gates; never auto-promote sandbox"),
    },
    {
        "id": "candidate_fail",
        "when": {"candidate_stage": "checked_fail"},
        "spawn": [
            {"job": "prune_rebuild", "relation": "serial"},
            {"job": "salvage_lessons", "relation": "parallel"},
        ],
        "rewrite": ("recurrence:candidate_followup", "narrow to earliest failed assumption; retain failed branch; do not repeat identical check"),
    },
    {
        "id": "receipt_gate",
        "when": {"event_tag": "temporary_lease"},
        "spawn": [
            {"job": "verify_durable_output_receipt", "relation": "gated"},
            {"job": "restore_displaced_lease", "relation": "gated", "depends_on": "verify_durable_output_receipt"},
        ],
        "rewrite": ("recurrence:lease_return", "restore only after durable output receipt OR explicit failure packet"),
    },
    {
        "id": "nested_learning",
        "when": {"event_tag": "learning"},
        "spawn": [
            {"job": "perform_bounded_work", "relation": "serial", "depth": 1,
             "on_result": {
                 "spawn": [
                     {"job": "extract_candidate_lesson", "relation": "serial", "depth": 2},
                     {"job": "transfer_test_second_locale", "relation": "perpendicular", "share": False, "depth": 2},
                 ]
             }},
        ],
        "rewrite": ("recurrence:actor_education", "only transfer-tested lesson becomes sticky; otherwise local note"),
    },
]

BASE_STATE = {
    "current_task": "advance one sandboxed theory candidate toward a discriminating check",
    "capabilities": ["repo_read", "repo_write", "python", "web_search", "automation_leases", "plugin_directory"],
    "blockers": [],
    "directives": [{
        "id": "WAR_ROOM_DECLARATION_2026-09-24",
        "source": "HSH_RESOURCES/HQ/THE_WAR_ROOM/DECLARATION.txt",
        "fresh": True,
        "incorporated": False,
    }],
    "theory_candidate": {"id": "candidate-geometry-001", "stage": "constructed", "checks": {}},
    "experience": {},
    "hydra_history": [],
}

SCENARIOS = {
    "missed_directive": ("Comptroller", "theory_workbench", {"tags": ["current", "directive", "notice"], "requires": ["repo_read"]}, {}),
    "comptroller_math": ("Comptroller", "math_toolbox", {"tags": ["math", "theory_candidate"], "requires": ["python"]}, {"directives": []}),
    "orson_math": ("Orson Vey", "math_toolbox", {"tags": ["math", "theory_candidate", "learning"], "requires": ["python"]}, {"directives": []}),
    "locker_override": ("Meridian", "epistemic_locker", {"tags": ["audit"], "workspace_override": {"purpose": "test unusual counterexample", "expires_after": "one quantum", "note": "compare with ordinary locker interpretation"}}, {"directives": []}),
    "capability_awareness": ("Comptroller", "theory_workbench", {"tags": ["blocked", "capability", "tool", "plugin"], "requires": ["multi_page_crawl"]}, {"directives": [], "blockers": ["missing dedicated crawl primitive"]}),
    "nested_learning": ("Orson Vey", "playground", {"tags": ["learning", "continuity"], "hydra_depth": 0}, {"directives": []}),
    "lease_receipt_gate": ("Comptroller", "theory_workbench", {"tags": ["temporary_lease"]}, {"directives": []}),
}

@dataclass
class Wake:
    actor: str
    locale: str
    workspace: str
    source_routes: list[str]
    fresh_directives: list[str]
    current_task: str
    blockers: list[str]
    capabilities: list[str]
    missing_capabilities: list[str]
    active_rules: list[str]
    next_operation: str

class Switchboard:
    def __init__(self, state: dict[str, Any] | None = None):
        self.state = copy.deepcopy(state or BASE_STATE)
        if TOP["mutation"] != "locked":
            raise ValueError("TOP must be locked")

    def source_routes(self, event: dict[str, Any]) -> list[str]:
        tags = set(event.get("tags", [])); wanted = set()
        if tags & {"directive", "current", "notice"}: wanted |= {"directive", "control"}
        if tags & {"planning", "priority"}: wanted |= {"planning", "priority"}
        if tags & {"identity", "continuity", "learning"}: wanted |= {"identity", "continuity", "experience"}
        if tags & {"blocked", "capability", "tool", "plugin"} or event.get("requires"): wanted |= {"tool", "plugin", "skill", "capability"}
        if tags & {"archive", "history", "provenance"}: wanted |= {"history", "provenance", "conversation"}
        out = [name for name, spec in SOURCES.items() if wanted & spec["kinds"]]
        if "directive" in wanted and "war_room" in out:
            out.remove("war_room"); out.insert(0, "war_room")
        return out[:4]

    def wake(self, actor: str, locale: str, event: dict[str, Any]) -> Wake:
        a = ACTORS[actor]; loc = LOCALES[locale]
        fresh = [d["id"] for d in self.state.get("directives", []) if d.get("fresh") and not d.get("incorporated")]
        caps = sorted(set(self.state.get("capabilities", [])))
        missing = sorted((set(event.get("requires", [])) | loc["requires"]) - set(caps))
        rules = TOP["rules"] + loc["rules"] + a["rules"] + loc["actor"].get(actor, []) + self.override_rules(loc, event)
        if fresh: nxt = "incorporate_fresh_directive"
        elif missing: nxt = "capability_scout"
        elif self.state.get("blockers"): nxt = "resolve_highest_blocker"
        else: nxt = event.get("requested_operation", self.state.get("current_task", "UNSET"))
        return Wake(actor, locale, a["workspace"], self.source_routes(event), fresh,
                    self.state.get("current_task", "UNSET"), list(self.state.get("blockers", [])),
                    caps, missing, rules, nxt)

    @staticmethod
    def override_rules(loc: dict[str, Any], event: dict[str, Any]) -> list[str]:
        o = event.get("workspace_override")
        if not o: return []
        if not loc["override"]: return ["OVERRIDE_REJECTED: locale locked"]
        if not {"purpose", "expires_after", "note"}.issubset(o): return ["OVERRIDE_REJECTED: incomplete"]
        return [f"BOUNDED_OVERRIDE:{o['purpose']}", f"EXPIRES:{o['expires_after']}", f"NOTE:{o['note']}"]

    def route(self, wake: Wake, event: dict[str, Any]) -> list[dict[str, Any]]:
        tags = set(event.get("tags", [])); out = []
        if wake.fresh_directives:
            out.append({"branch": "directive_intake", "relation": "serial", "share": True, "reason": "fresh directive"})
        if wake.missing_capabilities:
            out.append({"branch": "capability_scout", "relation": "parallel", "share": True, "reason": "missing capability"})
        seen = {x["branch"] for x in out}
        for name, spec in BRANCHES.items():
            if name not in seen and tags & spec["tags"]:
                out.append({"branch": name, "relation": spec["relation"], "share": spec["share"], "reason": sorted(tags & spec["tags"])})
        if self.state.get("theory_candidate", {}).get("stage") == "constructed" and "theory_candidate" in tags:
            for name in ("math_check", "adversarial_audit", "provenance_prior_art"):
                if name not in {x["branch"] for x in out}:
                    out.append({"branch": name, "relation": "perpendicular", "share": False, "reason": "independent candidate check"})
        return out

    def apply_checks(self, results: dict[str, dict[str, str]]) -> None:
        c = self.state.setdefault("theory_candidate", {}); checks = c.setdefault("checks", {})
        checks.update(results)
        req = ("math_check", "adversarial_audit", "provenance_prior_art")
        if all(k in checks for k in req):
            c["stage"] = "checked_pass" if all(checks[k].get("status") == "pass" for k in req) else "checked_fail"

    def sticky(self, actor: str, kind: str, text: str) -> None:
        if kind not in {"skill", "failure_mode", "tip", "goal", "intent", "education"}: raise ValueError(kind)
        fp = hashlib.sha256(f"{kind}:{text}".encode()).hexdigest()[:16]
        bag = self.state.setdefault("experience", {}).setdefault(actor, [])
        if fp not in {x["id"] for x in bag}: bag.append({"id": fp, "kind": kind, "text": text})

    def condition(self, cond: dict[str, Any], event: dict[str, Any]) -> bool:
        if "event_tag" in cond and cond["event_tag"] not in event.get("tags", []): return False
        if "fresh_directive" in cond:
            actual = any(d.get("fresh") and not d.get("incorporated") for d in self.state.get("directives", []))
            if actual != cond["fresh_directive"]: return False
        if "candidate_stage" in cond and self.state.get("theory_candidate", {}).get("stage") != cond["candidate_stage"]: return False
        return True

    def hydra(self, event: dict[str, Any]) -> dict[str, Any]:
        out = {"spawn": [], "rewrite": [], "guards": []}; max_depth = 3; rewrite_budget = 2
        history = self.state.setdefault("hydra_history", []); rewrites = 0
        for node in HYDRA_NODES:
            if not self.condition(node["when"], event): continue
            statekey = json.dumps({"node": node["id"], "stage": self.state.get("theory_candidate", {}).get("stage"), "directives": [(d["id"], d.get("incorporated")) for d in self.state.get("directives", [])]}, sort_keys=True)
            fp = hashlib.sha256(statekey.encode()).hexdigest()[:16]
            if fp in history:
                out["guards"].append(f"loop_guard:{node['id']}"); continue
            for raw in node.get("spawn", []):
                x = copy.deepcopy(raw); depth = int(x.get("depth", event.get("hydra_depth", 0) + 1))
                if depth > max_depth: out["guards"].append(f"depth_guard:{node['id']}:{depth}>{max_depth}"); continue
                x["depth"] = depth; out["spawn"].append(x)
            if node.get("rewrite") and rewrites < rewrite_budget:
                target, definition = node["rewrite"]
                if target == "TOP": out["guards"].append(f"top_lock:{node['id']}")
                else: out["rewrite"].append({"target": target, "definition": definition}); rewrites += 1
            history.append(fp)
        return out

def run(name: str) -> dict[str, Any]:
    actor, locale, event, patch = SCENARIOS[name]
    state = copy.deepcopy(BASE_STATE); state.update(copy.deepcopy(patch)); b = Switchboard(state)
    wake = b.wake(actor, locale, event)
    if name == "candidate_pass": pass
    return {"scenario": name, "wake": asdict(wake), "branches": b.route(wake, event), "hydra": b.hydra(event)}

def candidate_scenario(passed: bool) -> dict[str, Any]:
    state = copy.deepcopy(BASE_STATE); state["directives"] = []; b = Switchboard(state)
    status = "pass" if passed else "fail"
    b.apply_checks({
        "math_check": {"status": status if not passed else "pass"},
        "adversarial_audit": {"status": "pass"},
        "provenance_prior_art": {"status": "pass"},
    })
    event = {"tags": ["theory_candidate", "prediction", "paper"] if passed else ["theory_candidate", "failed_check", "prune"]}
    wake = b.wake("Meridian", "theory_workbench", event)
    return {"candidate": b.state["theory_candidate"], "branches": b.route(wake, event), "hydra": b.hydra(event)}

def self_test() -> dict[str, bool]:
    m = run("missed_directive")
    c = run("comptroller_math"); o = run("orson_math")
    f = candidate_scenario(False); p = candidate_scenario(True)
    r = run("lease_receipt_gate"); n = run("nested_learning")
    return {
        "directive_preempts": m["wake"]["next_operation"] == "incorporate_fresh_directive",
        "war_room_first": m["wake"]["source_routes"][0] == "war_room",
        "actor_overlays_differ": c["wake"]["active_rules"] != o["wake"]["active_rules"],
        "failed_candidate_prunes": any(x["job"] == "prune_rebuild" for x in f["hydra"]["spawn"]),
        "passed_candidate_papers": {"prediction_packet", "paper_pipeline"}.issubset({x["job"] for x in p["hydra"]["spawn"]}),
        "lease_has_receipt_gate": {"verify_durable_output_receipt", "restore_displaced_lease"}.issubset({x["job"] for x in r["hydra"]["spawn"]}),
        "nested_depth_present": any(x.get("depth") == 1 and x["job"] == "perform_bounded_work" for x in n["hydra"]["spawn"]),
    }

def main() -> None:
    p = argparse.ArgumentParser(); sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("demo"); sub.add_parser("self-test"); s = sub.add_parser("scenario"); s.add_argument("name")
    a = p.parse_args()
    if a.cmd == "scenario":
        print(json.dumps(run(a.name), indent=2)); return
    if a.cmd == "self-test":
        checks = self_test(); print(json.dumps({"ok": all(checks.values()), "checks": checks}, indent=2)); raise SystemExit(0 if all(checks.values()) else 1)
    for name in SCENARIOS:
        print(json.dumps(run(name), indent=2))
    print(json.dumps({"candidate_fail": candidate_scenario(False), "candidate_pass": candidate_scenario(True)}, indent=2))

if __name__ == "__main__":
    main()
