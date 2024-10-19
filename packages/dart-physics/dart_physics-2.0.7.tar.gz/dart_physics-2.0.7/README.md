# DART-Physics

![](./assets/dexhub.png)

This is a MuJoCo-based Physics Engine compatible with [DART](). 
You can launch this on a cloud server through [dexhub.ai](https://dexhub.ai) or run locally on your machine. 

### Launching Physics Engine
![](./assets/choices.png)
1. On the Cloud: Visit [dexhub.ai](https://dexhub.ai) and request a cloud-running physics engine. 
2. On your local machine: 
    ```
    pip install dart_physics
    python -m dart_physics.server 
    ```

### Acknowledgements

This project was possible thanks to the following open-source projects:

- [MuJoCo](https://mujoco.org/)
- High-fidelity MuJoCo robot models are from [MuJoCo Menagerie](https://github.com/deepmind/mujoco_menagerie).
- DART app on VisionOS is forked from [Tracking Streamer](https://github.com/dexhub-ai/tracking-streamer).
- IK solver is based on [mink](https://github.com/younghyo-park/mink).

