#!/usr/bin/env python3
"""
Diagnostic tool to check UraxLaw initialization status.

This tool helps developers verify that their UraxLaw instance is properly
initialized before use, preventing common initialization errors.

Usage:
    python -m uraxlaw.tools.check_initialization
"""

import asyncio
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from uraxlaw import UraxLaw
from uraxlaw.base import StoragesStatus


async def check_uraxlaw_setup(rag_instance: UraxLaw, verbose: bool = False) -> bool:
    """
    Check if a UraxLaw instance is properly initialized.

    Args:
        rag_instance: The UraxLaw instance to check
        verbose: If True, print detailed diagnostic information

    Returns:
        True if properly initialized, False otherwise
    """
    issues = []
    warnings = []

    print("🔍 Checking UraxLaw initialization status...\n")

    # Check storage initialization status
    if not hasattr(rag_instance, "_storages_status"):
        issues.append("UraxLaw instance missing _storages_status attribute")
    elif rag_instance._storages_status != StoragesStatus.INITIALIZED:
        issues.append(
            f"Storages not initialized (status: {rag_instance._storages_status.name})"
        )
    else:
        print("✅ Storage status: INITIALIZED")

    # Check individual storage components
    storage_components = [
        ("full_docs", "Document storage"),
        ("text_chunks", "Text chunks storage"),
        ("entities_vdb", "Entity vector database"),
        ("relationships_vdb", "Relationship vector database"),
        ("chunks_vdb", "Chunks vector database"),
        ("doc_status", "Document status tracker"),
        ("llm_response_cache", "LLM response cache"),
        ("full_entities", "Entity storage"),
        ("full_relations", "Relation storage"),
        ("chunk_entity_relation_graph", "Graph storage"),
    ]

    if verbose:
        print("\n📦 Storage Components:")

    for component, description in storage_components:
        if not hasattr(rag_instance, component):
            issues.append(f"Missing storage component: {component} ({description})")
        else:
            storage = getattr(rag_instance, component)
            if storage is None:
                warnings.append(f"Storage {component} is None (might be optional)")
            elif hasattr(storage, "_storage_lock"):
                if storage._storage_lock is None:
                    issues.append(f"Storage {component} not initialized (lock is None)")
                elif verbose:
                    print(f"  ✅ {description}: Ready")
            elif verbose:
                print(f"  ✅ {description}: Ready")

    # Check pipeline status
    try:
        from uraxlaw.kg.shared_storage import get_namespace_data

        get_namespace_data("pipeline_status")
        print("✅ Pipeline status: INITIALIZED")
    except KeyError:
        issues.append(
            "Pipeline status not initialized - call initialize_pipeline_status()"
        )
    except Exception as e:
        issues.append(f"Error checking pipeline status: {str(e)}")

    # Print results
    print("\n" + "=" * 50)

    if issues:
        print("❌ Issues found:\n")
        for issue in issues:
            print(f"  • {issue}")

        print("\n📝 To fix, run this initialization sequence:\n")
        print("  await rag.initialize_storages()")
        print("  from uraxlaw.kg.shared_storage import initialize_pipeline_status")
        print("  await initialize_pipeline_status()")
        print(
            "\n📚 Documentation: https://github.com/HKUDS/UraxLaw#important-initialization-requirements"
        )

        if warnings and verbose:
            print("\n⚠️  Warnings (might be normal):")
            for warning in warnings:
                print(f"  • {warning}")

        return False
    else:
        print("✅ UraxLaw is properly initialized and ready to use!")

        if warnings and verbose:
            print("\n⚠️  Warnings (might be normal):")
            for warning in warnings:
                print(f"  • {warning}")

        return True


async def demo():
    """Demonstrate the diagnostic tool with a test instance."""
    from uraxlaw.llm.openai import openai_embed, gpt_4o_mini_complete
    from uraxlaw.kg.shared_storage import initialize_pipeline_status

    print("=" * 50)
    print("UraxLaw Initialization Diagnostic Tool")
    print("=" * 50)

    # Create test instance
    rag = UraxLaw(
        working_dir="./test_diagnostic",
        embedding_func=openai_embed,
        llm_model_func=gpt_4o_mini_complete,
    )

    print("\n🔴 BEFORE initialization:\n")
    await check_uraxlaw_setup(rag, verbose=True)

    print("\n" + "=" * 50)
    print("\n🔄 Initializing...\n")
    await rag.initialize_storages()
    await initialize_pipeline_status()

    print("\n🟢 AFTER initialization:\n")
    await check_uraxlaw_setup(rag, verbose=True)

    # Cleanup
    import shutil

    shutil.rmtree("./test_diagnostic", ignore_errors=True)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Check UraxLaw initialization status")
    parser.add_argument(
        "--demo", action="store_true", help="Run a demonstration with a test instance"
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Show detailed diagnostic information",
    )

    args = parser.parse_args()

    if args.demo:
        asyncio.run(demo())
    else:
        print("Run with --demo to see the diagnostic tool in action")
        print("Or import this module and use check_uraxlaw_setup() with your instance")
