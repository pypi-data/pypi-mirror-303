
import sys
from dart_physics.robot_cfgs import GeomInfo
from scipy.spatial.transform import Rotation as R
import random
from pathlib import Path
from dart_physics.utils.run_functions import * 

HERE = Path(__file__).parent.absolute()


def random_xyz(i, xmin, xmax, ymin, ymax, zmin = 0.1):
    return [random.uniform(xmin, xmax), random.uniform(ymin, ymax), zmin + 0.02 * i ]

def duplicate_objects(name, num_max): 

    objs =  [name + "_{}".format(i) if i>0 else name for i in range(num_max)]

    # replicate the object 
    import shutil 
    obj_path = f"{HERE}/../assets/custom/{name}/{name}"
    
    for i in range(len(objs)):
        copy_path = f"{HERE}/../assets/custom/{name}_{i}"
        try: 
            shutil.copytree(obj_path, copy_path)
            shutil.move(f"{copy_path}/{name}.xml", f"{copy_path}/{name}_{i}.xml")
            # change the model name in the xml file
        except: 
            pass 
        # change the xml file (name.xml) to (name{i}.xml)

    return objs

def reset_function(model, data, robot_cfg, task_cfg): 

    id = robot_cfg["obj_startidx"] 
    vid = robot_cfg["obj_startidx"] 

    choices = [-0.13, -0.07, 0.0, 0.07, 0.13]

    for ii, obj in enumerate(task_cfg['objects']): 

        if obj == "all_pegs": 

            new_pos = task_cfg["default_poses"][obj][:3]   
            new_quat = R.from_euler('xyz', [0, 0, 0], degrees = True).as_quat(scalar_first = True).tolist()

        else:
            new_pos = task_cfg["default_poses"][obj][:3]
            # choose the x position from the choices list, shouldn't be replaced. 
            new_pos[0] = random.choice(choices)
            choices.remove(new_pos[0])

            new_quat = R.from_euler('xyz', [0, 0, np.random.randint(180)], degrees = True).as_quat(scalar_first = True).tolist()

        print(obj, len(new_pos))
        data.qpos[id:id+3] = new_pos
        data.qpos[id+3:id+7] = new_quat
        data.qvel[vid:vid+6] = 0.0

        id += 7 
        vid += 6


# utensils = duplicate_objects("toy_five_insertion_two", 1) + duplicate_objects("toy_five_insertion_four", 2) + duplicate_objects("toy_five_insertion_five", 2)

task_cfg = { 
    "name": "toy_five_insertions", 

    "objects": ["all_pegs", 
                "two_hole", 
                "one_hole", 
                "five_hole",
                "four_hole",  
                "three_hole", 
                # "toy_five_insertion_four_1", 
                # "toy_five_insertion_five", 
                # "toy_five_insertion_three", 
                # "toy_five_insertion_five_1"
                ], 

    "cone": "elliptic", 
    "o_solref": ".0000001 1",
    "o_solimp": ".001 1",
    "impratio": "1000.0",
    "multiccd": "enable" ,
    "override": "enable",

    "default_poses": {
        "all_pegs":  [0.01, 0.4, 0.1 ] + R.from_euler('xyz', [0, 0, 0], degrees = True).as_quat(scalar_first = True).tolist(), 

        "three_hole":   [-0.13, 0.3, 0.15 ] + R.from_euler('xyz', [0, 0, 0], degrees = True).as_quat(scalar_first = True).tolist(),
        "two_hole":   [-0.07, 0.3, 0.12] + R.from_euler('xyz', [0, 0, 0], degrees = True).as_quat(scalar_first = True).tolist(),
        "five_hole": [+0.13, 0.3, 0.14] + R.from_euler('xyz', [0, 0, 0], degrees = True).as_quat(scalar_first = True).tolist(),
        "four_hole":  [+0.0, 0.3, 0.16] + R.from_euler('xyz', [0, 0, 0], degrees = True).as_quat(scalar_first = True).tolist(),
        "one_hole":  [+0.07, 0.3, 0.18] + R.from_euler('xyz', [0, 0, 0], degrees = True).as_quat(scalar_first = True).tolist(),
        # "toy_five_insertion_five_1":  [+0.23, 0.3, 0.18] + R.from_euler('xyz', [0, 0, 0], degrees = True).as_quat(scalar_first = True).tolist(),
    }, 

    "reset_function": reset_function, 
    
}

# task_cfg["default_poses"].update({obj: random_xyz(i) + R.from_euler('xyz', [0, 0, np.random.randint(180)], degrees = True).as_quat(scalar_first = True).tolist() for i, obj in enumerate(utensils)})



if __name__ == "__main__":


    from runs import * 
    from utils.scene_gen import construct_scene
    import mujoco
    from loop_rate_limiters import RateLimiter


    robot = "dual_panda"
    robot_cfg = load_robot_cfg(robot)

    model = construct_scene(task_cfg, robot_cfg)
    data = mujoco.MjData(model)

    viewer = mujoco.viewer.launch_passive(
        model=model, data=data, show_left_ui=True, show_right_ui=True)
    
    mujoco.mj_resetDataKeyframe(model, data, 0)
    mujoco.mj_forward(model, data)
    mujoco.mj_camlight(model, data)

    rate = RateLimiter(500)
    while True:
        mujoco.mj_step(model, data)
        viewer.sync()
        rate.sleep()
    