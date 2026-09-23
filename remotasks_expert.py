"""
MARK-LIII â€” Remotasks Expert

Offline-first Remotasks knowledge plugin.

Design:
- Stable/general Remotasks concepts are answered from local knowledge.
- Current/live/account-specific questions are routed to the existing
  plugins.ai_provider interface.
- No direct network implementation is embedded here.
- No main.py modification is required.
"""

from __future__ import annotations

from typing import Any


PLUGIN = {
    "name": "remotasks_expert",
    "description": (
        "Remotasks expert for account/dashboard concepts, onboarding, "
        "2D annotation, 3D annotation, LiDAR, point clouds, 3D cuboids, "
        "qualification, certification, QA, task workflow, and beginner "
        "guidance. Use local knowledge for stable concepts and the online "
        "AI provider for current, live, account-specific, or time-sensitive "
        "questions."
    ),
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "operation": {
                "type": "STRING",
                "description": (
                    "Operation: ask, search, status, online, explain, coach, qc, analyze_instructions, or visual_qc."
                ),
            },
            "query": {
                "type": "STRING",
                "description": "The Remotasks question or topic.",
            },
            "mode": {
                "type": "STRING",
                "description": "Mode: auto, offline, or online.",
            },
        },
        "required": [],
    },
}


# ---------------------------------------------------------------------------
# Stable offline knowledge
# ---------------------------------------------------------------------------

KNOWLEDGE: dict[str, dict[str, Any]] = {
    "basics": {
        "keywords": (
            "remotasks",
            "task",
            "tasks",
            "platform",
            "dashboard",
        ),
        "title": "Remotasks basics",
        "answer": (
            "Remotasks is a task-based data-work platform where qualified "
            "contributors may complete data annotation, collection, "
            "transcription, categorization, and related tasks. Project "
            "availability, qualification requirements, and task access can "
            "change, so current account/project status should be checked "
            "online rather than assumed from offline knowledge."
        ),
    },
    "dashboard": {
        "keywords": (
            "dashboard",
            "task log",
            "balance",
            "missions",
            "announcements",
            "feedback",
            "support",
        ),
        "title": "Dashboard and account areas",
        "answer": (
            "Common dashboard areas include task history/log information, "
            "balance or earnings information, onboarding or qualification "
            "areas, missions, feedback/support, and announcements. Exact "
            "menus and available projects can vary by account and over time."
        ),
    },
    "onboarding": {
        "keywords": (
            "onboarding",
            "qualification",
            "qualify",
            "qualification exam",
            "certification",
            "certification exam",
            "bootcamp",
            "training",
        ),
        "title": "Onboarding and qualification",
        "answer": (
            "Onboarding is where a contributor may encounter training, "
            "certification exams, bootcamps, or project-specific "
            "qualification steps. Passing a qualification does not "
            "guarantee that a project will remain available; access depends "
            "on the platform's current project allocation and account state."
        ),
    },
    "2d": {
        "keywords": (
            "2d",
            "image annotation",
            "image segmentation",
            "video annotation",
            "2d annotation",
        ),
        "title": "2D annotation",
        "answer": (
            "2D annotation works with ordinary images or video frames. "
            "Depending on the task, the contributor may mark objects, "
            "classify content, draw regions, or segment pixels. Accuracy "
            "depends on following the project's exact labeling instructions, "
            "class definitions, boundary rules, and quality checks."
        ),
    },
    "3d": {
        "keywords": (
            "3d",
            "3d annotation",
            "3d annotation task",
            "point cloud",
            "point clouds",
            "lidar",
            "lidar annotation",
            "lidar segmentation",
            "3d cuboid",
            "3d cuboids",
        ),
        "title": "3D and LiDAR annotation",
        "answer": (
            "3D annotation commonly works with point-cloud data, including "
            "LiDAR-derived point clouds. Typical work can include identifying "
            "objects, assigning classes, fitting 3D cuboids, or segmenting "
            "points according to project-specific rules. The exact workflow "
            "and allowed object classes are defined by the active project's "
            "instructions."
        ),
    },
    "lidar": {
        "keywords": (
            "lidar",
            "lidar annotation",
            "lidar segmentation",
            "point cloud",
            "point clouds",
            "3d cuboid",
            "3d bounding box",
        ),
        "title": "LiDAR workflow",
        "answer": (
            "For LiDAR annotation, first understand the project's object "
            "classes and visibility rules. Inspect the point cloud from "
            "multiple views, identify the complete object extent, place or "
            "adjust the 3D annotation according to the project guide, and "
            "check orientation, dimensions, class, and occlusion/visibility "
            "before submitting. Do not invent class definitions when the "
            "active project provides a specific taxonomy."
        ),
    },
    "quality": {
        "keywords": (
            "quality",
            "qa",
            "accuracy",
            "mistake",
            "errors",
            "annotation accuracy",
            "quality assurance",
        ),
        "title": "Annotation quality",
        "answer": (
            "Annotation quality is generally more important than simply "
            "working quickly. Before submission, verify the object class, "
            "annotation boundaries, placement, dimensions/orientation where "
            "applicable, visibility/occlusion labels, and any project-specific "
            "rules. Repeated errors can affect qualification or access when "
            "the active project uses quality gates."
        ),
    },
    "beginner": {
        "keywords": (
            "beginner",
            "newbie",
            "starting",
            "start",
            "how to start",
            "first task",
            "first project",
        ),
        "title": "Beginner path",
        "answer": (
            "A practical beginner path is: complete the account/profile "
            "requirements, inspect the available onboarding options, study "
            "the project instructions carefully, complete the required "
            "qualification or training, and start with the task type that "
            "your account actually makes available. For 3D/LiDAR work, "
            "practice point-cloud orientation, object recognition, 3D "
            "cuboids, and careful quality checking before optimizing speed."
        ),
    },
    "payments": {
        "keywords": (
            "payment",
            "payments",
            "payout",
            "payouts",
            "paypal",
            "airtm",
            "earnings",
            "balance",
        ),
        "title": "Payments",
        "answer": (
            "Payment methods, payout eligibility, minimums, timing, and "
            "available options are account/platform dependent and can change. "
            "Use the current payment section of the account for authoritative "
            "information. Offline knowledge should not be used to promise a "
            "specific payout amount or payment method."
        ),
    },
    "projects": {
        "keywords": (
            "project",
            "projects",
            "active project",
            "available project",
            "task availability",
            "no active project",
            "project access",
        ),
        "title": "Project availability",
        "answer": (
            "Project availability is dynamic. A contributor can complete "
            "onboarding or qualification and still have no active project "
            "available at a particular time. Current project availability "
            "must be checked against the live account/dashboard."
        ),
    },
}


SPECIALIST_KNOWLEDGE: dict[str, dict[str, Any]] = {
    "lidar_geometry": {
        "title": "LiDAR and 3D geometry",
        "keywords": [
            "lidar", "point cloud", "pointcloud", "3d", "cuboid",
            "bounding box", "heading", "yaw", "rotation",
            "length", "width", "height", "dimensions", "center",
        ],
        "content": (
            "LiDAR/3D annotation commonly uses point-cloud geometry. "
            "A 3D cuboid should fit the visible object according to the "
            "active project's coordinate, orientation, size, and class rules. "
            "Check object center, dimensions, heading/yaw, ground contact, "
            "and alignment with the point cloud."
        ),
    },
    "occlusion": {
        "title": "Occlusion and visibility",
        "keywords": [
            "occlusion", "occluded", "hidden", "blocked",
            "partially visible", "truncated", "visibility",
        ],
        "content": (
            "For partially occluded objects, follow the project's exact "
            "occlusion and visibility policy. Do not invent hidden geometry. "
            "Use visible evidence and project-specific rules to decide whether "
            "the object should be labeled and how its 3D box should be fitted."
        ),
    },
    "segmentation": {
        "title": "Segmentation",
        "keywords": [
            "segmentation", "segment", "segments", "points",
            "point segmentation", "semantic", "instance",
        ],
        "content": (
            "Segmentation assigns points or regions to project-defined classes. "
            "Keep boundaries consistent, avoid including neighboring objects, "
            "and follow the active project's class definitions and edge rules."
        ),
    },
    "consistency": {
        "title": "Annotation consistency",
        "keywords": [
            "consistency", "consistent", "same object", "same class",
            "frame", "frames", "tracking", "annotation standard",
        ],
        "content": (
            "Consistent annotation means applying the same project rules across "
            "objects and frames. Check class naming, cuboid placement, dimensions, "
            "orientation, visibility handling, and boundary decisions against "
            "the project's instructions."
        ),
    },
    "common_errors": {
        "title": "Common annotation errors",
        "keywords": [
            "mistake", "mistakes", "error", "errors", "wrong",
            "bad annotation", "quality", "qa", "qc", "rejection",
        ],
        "content": (
            "Common errors include wrong class selection, loose or oversized "
            "3D boxes, incorrect orientation, poor ground alignment, missed "
            "objects, accidental inclusion of neighboring points, inconsistent "
            "occlusion handling, and failure to follow project-specific rules."
        ),
    },
}


def _specialist_search(query: str) -> str:
    q = _normalize(query)

    if not q:
        return "Please provide a Remotasks annotation question."

    matches: list[tuple[int, str, dict[str, Any]]] = []

    for key, item in SPECIALIST_KNOWLEDGE.items():
        score = 0

        for keyword in item["keywords"]:
            if keyword in q:
                score += 1

        if score:
            matches.append((score, key, item))

    if not matches:
        return _search_local(query)

    matches.sort(key=lambda x: (-x[0], x[1]))

    score, key, item = matches[0]

    return (
        "REMOTASKS SPECIALIST\n"
        f"Topic: {item['title']}\n"
        f"Match score: {score}\n\n"
        f"{item['content']}\n\n"
        "Reminder: the active project's instructions always take priority "
        "over this general guidance."
    )


def _task_coach(query: str) -> str:
    project_guidance = _analyze_instructions(
        f"{query} annotation class geometry quality "
        "occlusion submission"
    )

    return (
        "REMOTASKS TASK COACH\n\n"
        "Before starting a task:\n"
        "1. Read the active project instructions carefully.\n"
        "2. Confirm the allowed object classes and annotation rules.\n"
        "3. Check examples or reference annotations if provided.\n"
        "4. Work systematically rather than guessing ambiguous objects.\n"
        "5. Before submitting, perform a QC pass for class, geometry, "
        "visibility, boundaries, and consistency.\n\n"
        f"Task/question: {query}\n\n"
        "PROJECT-SPECIFIC GUIDANCE\n\n"
        f"{project_guidance}\n\n"
        "Project instruction files are authoritative. "
        "If a required rule is not present, do not invent one."
    )


def _qc_checklist(query: str) -> str:
    project_guidance = _analyze_instructions(
        f"{query} quality qc class annotation geometry "
        "occlusion submission verify"
    )

    return (
        "REMOTASKS QC CHECKLIST\n\n"
        "Generic QC baseline:\n"
        "Class:\n"
        "- Correct class selected?\n"
        "- Class allowed by the project?\n\n"
        "Geometry:\n"
        "- 3D box fits the object?\n"
        "- Length/width/height reasonable?\n"
        "- Center and ground contact correct?\n"
        "- Orientation/heading correct?\n\n"
        "Visibility:\n"
        "- Occlusion handled according to project rules?\n"
        "- No unsupported hidden geometry invented?\n\n"
        "Segmentation/boundaries:\n"
        "- Correct points included?\n"
        "- Neighboring objects excluded?\n"
        "- Boundaries consistent?\n\n"
        "Consistency:\n"
        "- Same rules applied across frames/objects?\n"
        "- No obvious missed or duplicate annotations?\n\n"
        f"QC target: {query}\n\n"
        "PROJECT-SPECIFIC QC GUIDANCE\n\n"
        f"{project_guidance}\n\n"
        "Final authority: the active project's instructions."
    )


def _instruction_files():
    from pathlib import Path

    project_dir = (
        Path(__file__).resolve().parent
        / "remotasks_project_instructions"
    )

    if not project_dir.exists():
        return []

    return sorted(
        [
            p for p in project_dir.rglob("*")
            if p.is_file()
            and p.suffix.lower() in {".txt", ".md", ".json"}
        ],
        key=lambda p: str(p).lower(),
    )


def _analyze_instructions(query: str) -> str:
    files = _instruction_files()

    if not files:
        from pathlib import Path

        project_dir = (
            Path(__file__).resolve().parent
            / "remotasks_project_instructions"
        )

        return (
            "REMOTASKS PROJECT INSTRUCTIONS\n\n"
            "No local project-instruction files were found.\n\n"
            "Expected folder:\n"
            f"{project_dir}\n\n"
            "Add project instruction files there, then run "
            "analyze_instructions again.\n\n"
            f"Question: {query}"
        )

    normalized_query = _normalize(query)

    query_terms = [
        term
        for term in normalized_query.split()
        if len(term) >= 3
    ]

    term_groups = {
        "cuboid": {
            "cuboid",
            "box",
            "boxes",
            "bounding",
            "geometry",
        },
        "quality": {
            "quality",
            "qc",
            "check",
            "verify",
            "verification",
            "mistake",
            "mistakes",
            "accuracy",
        },
        "occlusion": {
            "occlusion",
            "occluded",
            "occlude",
            "visibility",
            "visible",
        },
        "submission": {
            "submit",
            "submission",
            "before",
            "final",
        },
        "class": {
            "class",
            "classes",
            "category",
            "categories",
            "object",
        },
        "annotation": {
            "annotation",
            "annotate",
            "annotated",
            "label",
            "labels",
        },
    }

    active_groups: set[str] = set()

    for group_name, group_terms in term_groups.items():
        if any(
            term in group_terms
            or any(
                term.startswith(candidate)
                or candidate.startswith(term)
                for candidate in group_terms
            )
            for term in query_terms
        ):
            active_groups.add(group_name)

    matches: list[tuple[int, str, str]] = []
    fallbacks: list[tuple[str, str]] = []

    for path in files[:10]:
        try:
            content = path.read_text(
                encoding="utf-8",
                errors="replace",
            )
        except Exception:
            continue

        for line in content.splitlines():
            cleaned = " ".join(line.split())

            if not cleaned:
                continue

            fallbacks.append((path.name, cleaned))

            normalized_line = _normalize(cleaned)

            # Ignore heading-only lines such as:
            # "Quality:" / "Annotation rules:"
            heading_only = (
                cleaned.endswith(":")
                and not cleaned[:1].isdigit()
                and not cleaned.startswith(("-", "*", "â€¢"))
            )

            if heading_only:
                continue

            score = 0

            # Direct query-term matching.
            for term in query_terms:
                if term in normalized_line:
                    score += 2

            # Related terminology matching.
            for group_name in active_groups:
                group_terms = term_groups[group_name]

                if any(
                    term in normalized_line
                    for term in group_terms
                ):
                    score += 2

            # Morphological/context boosts.
            if "occlusion" in active_groups:
                if (
                    "occlud" in normalized_line
                    or "visible" in normalized_line
                    or "visibility" in normalized_line
                ):
                    score += 2

            if "submission" in active_groups:
                if (
                    "submit" in normalized_line
                    or "submission" in normalized_line
                    or "before" in normalized_line
                    or "final" in normalized_line
                ):
                    score += 2

            # Rule-like lines are more useful than plain prose.
            if (
                cleaned[:1].isdigit()
                or cleaned.startswith(("-", "*", "â€¢"))
            ):
                score += 1

            if score > 0:
                matches.append(
                    (score, path.name, cleaned)
                )

    if not matches:
        excerpts: list[str] = []

        for filename, line in fallbacks[:12]:
            excerpts.append(
                f"[FILE] {filename}\n{line[:500]}"
            )

        if not excerpts:
            return (
                "REMOTASKS PROJECT INSTRUCTIONS\n\n"
                "Instruction files were found, but none could be read."
            )

        return (
            "REMOTASKS PROJECT INSTRUCTION ANALYZER\n\n"
            f"Question: {query}\n\n"
            "No directly matching instruction lines were found.\n\n"
            + "\n\n".join(excerpts)
            + "\n\n"
            "Use the supplied project instructions as the authoritative "
            "source. This analyzer summarizes local files; it does not "
            "invent missing rules."
        )

    matches.sort(
        key=lambda item: (
            -item[0],
            item[1].lower(),
            item[2].lower(),
        )
    )

    selected: list[str] = []
    seen: set[tuple[str, str]] = set()

    for score, filename, line in matches[:12]:
        key = (filename, line)

        if key in seen:
            continue

        seen.add(key)

        selected.append(
            f"[FILE] {filename} | relevance={score}\n"
            f"{line[:700]}"
        )

    return (
        "REMOTASKS PROJECT INSTRUCTION ANALYZER\n\n"
        f"Question: {query}\n\n"
        "Relevant instruction lines:\n\n"
        + "\n\n".join(selected)
        + "\n\n"
        "Use the supplied project instructions as the authoritative "
        "source. This analyzer summarizes local files; it does not "
        "invent missing rules."
    )
CURRENT_MARKERS = (
    "today",
    "right now",
    "currently",
    "current",
    "latest",
    "recent",
    "this week",
    "this month",
    "active project",
    "available project",
    "my account",
    "my balance",
    "my dashboard",
    "my task",
    "my tasks",
    "payment status",
    "payout status",
    "latest requirement",
    "current requirement",
    "current rules",
    "latest rules",
    "announcement",
)


def _normalize(value: Any) -> str:
    return " ".join(str(value or "").lower().strip().split())


def _is_current_question(query: str) -> bool:
    text = _normalize(query)
    return any(marker in text for marker in CURRENT_MARKERS)


def _search_local(query: str) -> str:
    text = _normalize(query)

    if not text:
        return (
            "Please provide a Remotasks question or topic."
        )

    scored: list[tuple[int, str, str]] = []

    for key, item in KNOWLEDGE.items():
        score = 0

        for keyword in item["keywords"]:
            kw = _normalize(keyword)

            if kw and kw in text:
                # More specific phrases get more weight.
                score += 3 if " " in kw else 1

        if score:
            scored.append(
                (score, item["title"], item["answer"])
            )

    if not scored:
        return (
            f"No direct offline Remotasks knowledge match was found for: "
            f"{query}\n\n"
            "Try a topic such as dashboard, onboarding, 2D annotation, "
            "3D annotation, LiDAR, point clouds, 3D cuboids, QA, "
            "qualification, beginner steps, or payments."
        )

    scored.sort(key=lambda row: row[0], reverse=True)

    best_score, title, answer = scored[0]

    return (
        "REMOTASKS OFFLINE KNOWLEDGE\n"
        f"Topic: {title}\n"
        f"Match score: {best_score}\n\n"
        f"{answer}"
    )


def _online(prompt: str) -> str:
    try:
        from plugins.ai_provider import run as ai_provider_run

        result = ai_provider_run(
            {
                "action": "ask",
                "prompt": prompt,
                "system": (
                    "You are the Mark-LIII Remotasks Expert. "
                    "Answer factually and clearly. "
                    "For current account/project/payment/platform information, "
                    "do not invent facts. If the available information is "
                    "insufficient to verify something current, say so. "
                    "Separate stable Remotasks concepts from current claims."
                ),
            }
        )

        return str(result)

    except Exception as exc:
        return (
            "Online Remotasks lookup is unavailable right now.\n"
            f"Provider error: {exc}\n\n"
            "I can still answer stable Remotasks concepts from offline "
            "knowledge."
        )


def _status() -> str:
    return (
        "REMOTASKS EXPERT STATUS\n"
        "Mode: OFFLINE-FIRST / ONLINE-CAPABLE\n"
        f"Offline knowledge topics: {len(KNOWLEDGE)}\n"
        "Online interface: plugins.ai_provider\n"
        "Current/account-specific information: ONLINE REQUIRED\n"
        "main.py modification: NOT REQUIRED"
    )


def _visual_qc(image_path: str, query: str) -> str:
    """Run existing visual analysis and combine it with Remotasks QC guidance."""
    image_path = str(image_path or "").strip()
    query = str(query or "").strip()

    if not image_path:
        return "Please provide image_path for visual Remotasks QC."

    try:
        from plugins.visual_diy_expert import run as visual_run
    except Exception as exc:
        return f"Visual engine unavailable: {exc}"

    visual_question = (
        "Analyze this image specifically for Remotasks annotation QC. "
        "Report only what is visibly supported by the image. "
        "Check for visible annotation boxes/cuboids, apparent object-class "
        "issues, box coverage, oversized or undersized boxes, unrelated "
        "objects, visible occlusion concerns, and anything that should be "
        "manually verified before submission. "
        "Do not invent project rules, exact dimensions, hidden geometry, or "
        "object identities that cannot be established from the image. "
        f"Task context: {query or 'general Remotasks annotation QC'}"
    )

    try:
        visual_result = visual_run(
            {
                "action": "analyze",
                "image_path": image_path,
                "question": visual_question,
            }
        )
    except Exception as exc:
        return f"Visual analysis failed: {exc}"

    if isinstance(visual_result, dict):
        visual_text = str(
            visual_result.get("result")
            or visual_result.get("message")
            or visual_result
        )
    else:
        visual_text = str(visual_result)

    project_query = (
        f"{query or 'Remotasks annotation'} "
        "quality qc class annotation geometry occlusion submission verify"
    )

    try:
        project_guidance = _analyze_instructions(project_query)
    except Exception as exc:
        project_guidance = f"Project instruction analysis unavailable: {exc}"

    return (
        "REMOTASKS VISUAL QC\n\n"
        "IMAGE / VISION FINDINGS\n\n"
        f"{visual_text}\n\n"
        "PROJECT-SPECIFIC QC GUIDANCE\n\n"
        f"{project_guidance}\n\n"
        "FINAL VERIFICATION NOTE\n\n"
        "Visual findings are observations from the supplied image, not "
        "automatic ground truth. Verify class, geometry, occlusion, and "
        "project-specific requirements manually before submission. "
        "Do not treat image-only dimensions as exact without a reliable "
        "scale or reference."
    )


def run(
    parameters: dict | None = None,
    player=None,
    session_memory=None,
) -> str:
    try:
        p = dict(parameters or {})

        operation = _normalize(
            p.get("operation", "ask")
        )

        query = str(
            p.get("query")
            or p.get("prompt")
            or p.get("text")
            or ""
        ).strip()

        mode = _normalize(
            p.get("mode", "auto")
        )

        if operation == "status":
            return _status()

        if operation == "explain":
            if not query:
                return "Please provide a Remotasks annotation topic."
            return _specialist_search(query)

        if operation == "coach":
            if not query:
                return "Please provide the Remotasks task you want coaching for."
            return _task_coach(query)

        if operation == "qc":
            if not query:
                query = "general annotation"
            return _qc_checklist(query)

        if operation == "visual_qc":
            image_path = str(
                p.get("image_path")
                or p.get("image")
                or ""
            ).strip()

            if not image_path:
                return "Please provide image_path for visual Remotasks QC."

            return _visual_qc(image_path, query)

        if operation == "analyze_instructions":
            if not query:
                query = "project instructions"
            return _analyze_instructions(query)

        if operation == "online":
            if not query:
                return "Please provide a current Remotasks question."
            return _online(query)

        if operation == "search":
            return _search_local(query)

        if operation != "ask":
            return (
                "Unknown Remotasks operation. "
                "Use ask, search, online, explain, coach, qc, analyze_instructions, visual_qc, or status."
            )

        if not query:
            return "Please provide a Remotasks question."

        if mode == "online":
            return _online(query)

        if mode == "offline":
            return _search_local(query)

        # AUTO mode:
        # Current/live/account-specific requests go online.
        if _is_current_question(query):
            return _online(query)

        return _search_local(query)

    except Exception as exc:
        return f"Remotasks expert failed: {exc}"
