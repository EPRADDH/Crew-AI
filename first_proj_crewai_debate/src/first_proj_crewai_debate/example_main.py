#!/usr/bin/env python
"""
Example Main entry point for the Debate Crew AI application.
This module provides functions to run, train, replay, and test the debate crew.
This is an improved version with better error handling, CLI support, and documentation.
"""

import sys
import warnings
import argparse
from datetime import datetime
from typing import Dict, Any

from first_proj_crewai_debate.crew import Debate

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def get_default_inputs() -> Dict[str, Any]:
    """
    Get default inputs for the debate crew.
    
    Returns:
        Dict containing default input parameters
    """
    return {
        'motion': 'AI LLMs will significantly improve human productivity',
        'current_year': str(datetime.now().year)
    }


def validate_inputs(inputs: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validate and sanitize inputs.
    
    Args:
        inputs: Input dictionary to validate
        
    Returns:
        Validated input dictionary
    """
    if not inputs.get('motion'):
        inputs['motion'] = get_default_inputs()['motion']
    
    if not inputs.get('current_year'):
        inputs['current_year'] = get_default_inputs()['current_year']
    
    return inputs


def run(inputs: Dict[str, Any] = None) -> None:
    """
    Run the debate crew with the given inputs.
    
    Args:
        inputs: Optional input dictionary. If None, default inputs will be used.
    """
    if inputs is None:
        inputs = get_default_inputs()
    
    inputs = validate_inputs(inputs)
    
    print(f"Starting debate on motion: {inputs['motion']}")
    print(f"Current year: {inputs['current_year']}")
    print("-" * 50)
    
    try:
        crew_instance = Debate()
        result = crew_instance.crew().kickoff(inputs=inputs)
        print("\n" + "=" * 50)
        print("DEBATE COMPLETED")
        print("=" * 50)
        print(f"Result: {result}")
        
    except Exception as e:
        print(f"❌ Error occurred while running the crew: {e}")
        raise


def train(n_iterations: int = 5, filename: str = "training_results.json", inputs: Dict[str, Any] = None) -> None:
    """
    Train the debate crew for a given number of iterations.
    
    Args:
        n_iterations: Number of training iterations
        filename: Output filename for training results
        inputs: Optional input dictionary
    """
    if inputs is None:
        inputs = get_default_inputs()
    
    inputs = validate_inputs(inputs)
    
    print(f"Training crew for {n_iterations} iterations...")
    print(f"Motion: {inputs['motion']}")
    print(f"Results will be saved to: {filename}")
    print("-" * 50)
    
    try:
        crew_instance = Debate()
        crew_instance.crew().train(
            n_iterations=n_iterations, 
            filename=filename, 
            inputs=inputs
        )
        print(f"✅ Training completed successfully! Results saved to {filename}")
        
    except Exception as e:
        print(f"❌ Error occurred while training the crew: {e}")
        raise


def replay(task_id: str) -> None:
    """
    Replay the crew execution from a specific task.
    
    Args:
        task_id: ID of the task to replay from
    """
    print(f"Replaying crew execution from task: {task_id}")
    print("-" * 50)
    
    try:
        crew_instance = Debate()
        result = crew_instance.crew().replay(task_id=task_id)
        print(f"✅ Replay completed successfully!")
        print(f"Result: {result}")
        
    except Exception as e:
        print(f"❌ Error occurred while replaying the crew: {e}")
        raise


def test(n_iterations: int = 3, eval_llm: str = "openai/gpt-4o-mini", inputs: Dict[str, Any] = None) -> None:
    """
    Test the crew execution and return the results.
    
    Args:
        n_iterations: Number of test iterations
        eval_llm: LLM to use for evaluation
        inputs: Optional input dictionary
    """
    if inputs is None:
        inputs = get_default_inputs()
    
    inputs = validate_inputs(inputs)
    
    print(f"Testing crew for {n_iterations} iterations...")
    print(f"Evaluation LLM: {eval_llm}")
    print(f"Motion: {inputs['motion']}")
    print("-" * 50)
    
    try:
        crew_instance = Debate()
        result = crew_instance.crew().test(
            n_iterations=n_iterations, 
            eval_llm=eval_llm, 
            inputs=inputs
        )
        print(f"✅ Testing completed successfully!")
        print(f"Test results: {result}")
        
    except Exception as e:
        print(f"❌ Error occurred while testing the crew: {e}")
        raise


def main():
    """
    Main function to handle command line arguments and execute appropriate function.
    """
    parser = argparse.ArgumentParser(description="Debate Crew AI - Run, train, or test the debate crew")
    parser.add_argument("action", choices=["run", "train", "replay", "test"], 
                       help="Action to perform")
    parser.add_argument("--motion", type=str, 
                       help="Debate motion/topic")
    parser.add_argument("--iterations", type=int, default=5,
                       help="Number of iterations for train/test (default: 5)")
    parser.add_argument("--filename", type=str, default="training_results.json",
                       help="Output filename for training (default: training_results.json)")
    parser.add_argument("--eval-llm", type=str, default="openai/gpt-4o-mini",
                       help="LLM for evaluation (default: openai/gpt-4o-mini)")
    parser.add_argument("--task-id", type=str,
                       help="Task ID for replay action")
    
    args = parser.parse_args()
    
    # Prepare inputs
    inputs = get_default_inputs()
    if args.motion:
        inputs['motion'] = args.motion
    
    try:
        if args.action == "run":
            run(inputs)
        elif args.action == "train":
            train(args.iterations, args.filename, inputs)
        elif args.action == "replay":
            if not args.task_id:
                print("❌ Error: task-id is required for replay action")
                sys.exit(1)
            replay(args.task_id)
        elif args.action == "test":
            test(args.iterations, args.eval_llm, inputs)
            
    except KeyboardInterrupt:
        print("\n⚠️  Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # If no command line arguments, run with default settings
    if len(sys.argv) == 1:
        print("Running debate crew with default settings...")
        run()
    else:
        main() 