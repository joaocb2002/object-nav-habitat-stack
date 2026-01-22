from pathlib import Path
from objectnav.sim.simulator import make_sim

def main():
    # Launch simulator
    print("Launching simulator...")
    simulator = make_sim(scene_dataset_config=Path("datasets/ai2thor-hab/ai2thor-hab/ai2thor-hab.scene_dataset_config.json"), scene_id="FloorPlan1_physics")

    # Reset simulator
    print("Resetting simulator...")
    simulator.reset() 

    # Close simulator
    print("Closing simulator...")
    simulator.close()


if __name__ == "__main__":
    main()