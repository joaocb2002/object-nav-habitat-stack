from objectnav.sim.simulator import make_sim

def main():

    # Launch simulator
    sim = make_sim(scene_dataset_config=Path("/path/to/scene_dataset_config.json"), scene_id="scene_id")


if __name__ == "__main__":
    main()