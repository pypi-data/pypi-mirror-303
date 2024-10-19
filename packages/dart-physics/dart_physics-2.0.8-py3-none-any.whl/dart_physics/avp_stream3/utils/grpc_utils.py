import numpy as np 
from typing import * 
from dart_physics.avp_stream3.grpc_msg import *

def matrix4x4_to_proto(matrix: np.ndarray) -> dexterity_pb2.Matrix4x4:
    """
    input:  matrix: np.ndarray - a 4x4 numpy array
    output: handtracking_pb2.Matrix4x4 - a protobuf message
    does:   converts a 4x4 numpy array to a protobuf message


    message Matrix4x4 {
        float m00 = 1;
        float m01 = 2;
        float m02 = 3;
        float m03 = 4;
        float m10 = 5;
        float m11 = 6;
        float m12 = 7;
        float m13 = 8;
        float m20 = 9;
        float m21 = 10;
        float m22 = 11;
        float m23 = 12;
        float m30 = 13;
        float m31 = 14;
        float m32 = 15;
        float m33 = 16;
        }

    """
    proto_matrix = dexterity_pb2.Matrix4x4()
    proto_matrix.m00 = matrix[0, 0]
    proto_matrix.m01 = matrix[0, 1]
    proto_matrix.m02 = matrix[0, 2]
    proto_matrix.m03 = matrix[0, 3]
    proto_matrix.m10 = matrix[1, 0]
    proto_matrix.m11 = matrix[1, 1]
    proto_matrix.m12 = matrix[1, 2]
    proto_matrix.m13 = matrix[1, 3]
    proto_matrix.m20 = matrix[2, 0]
    proto_matrix.m21 = matrix[2, 1]
    proto_matrix.m22 = matrix[2, 2]
    proto_matrix.m23 = matrix[2, 3] 
    # proto_matrix.m30 = matrix[3, 0]
    # proto_matrix.m31 = matrix[3, 1]
    # proto_matrix.m32 = matrix[3, 2]
    # proto_matrix.m33 = matrix[3, 3]

    return proto_matrix



def process_matrix(message):
    m = np.array([[[message.m00, message.m01, message.m02, message.m03],
                    [message.m10, message.m11, message.m12, message.m13],
                    [message.m20, message.m21, message.m22, message.m23],
                    [0, 0, 0, 1]]])
    return m 

def process_matrices(skeleton, matrix = np.eye(4)):
    return np.concatenate([matrix @ process_matrix(joint) for joint in skeleton], axis = 0)


def rotate_head(R, degrees=-90):
    # Convert degrees to radians
    theta = np.radians(degrees)
    # Create the rotation matrix for rotating around the x-axis
    R_x = np.array([[
        [1, 0, 0, 0],
        [0, np.cos(theta), -np.sin(theta), 0],
        [0, np.sin(theta), np.cos(theta), 0],
        [0, 0, 0, 1]
    ]])
    R_rotated = R @ R_x 
    return R_rotated


def get_pinch_distance(finger_messages): 
    fingers = process_matrices(finger_messages)
    thumb = fingers[4, :3, 3]
    index = fingers[9, :3, 3]

    return np.linalg.norm(thumb - index)

def get_wrist_roll(mat):
    """
    returns roll, pitch, yaw in radians
    """
    R = mat[0, :3, :3]

    # Calculate angles for rotation around z and y axis to align the first column with [1, 0, 0]
    # Angle to rotate around z-axis to align the projection on the XY plane
    theta_z = np.arctan2(R[1, 0], R[0, 0])  # arctan2(y, x)

    # Rotate R around the z-axis by -theta_z to align its x-axis on the XY plane
    Rz = np.array([
        [np.cos(-theta_z), -np.sin(-theta_z), 0],
        [np.sin(-theta_z), np.cos(-theta_z), 0],
        [0, 0, 1]
    ])
    R_after_z = Rz @ R

    # Angle to rotate around y-axis to align the x-axis with the global x-axis
    theta_y = np.arctan2(R_after_z[0, 2], R_after_z[0, 0])  # arctan2(z, x)

    # Since the goal is to align the x-axis, the rotation around the x-axis might not be necessary
    # unless there are specific orientations required for the y and z axes after the alignment.

    # Calculated angles (converted to degrees for easier interpretation)
    theta_z_deg = np.degrees(theta_z)
    theta_y_deg = np.degrees(theta_y)

    Ry = np.array([
        [np.cos(-theta_y), 0, np.sin(-theta_y)],
        [0, 1, 0],
        [-np.sin(-theta_y), 0, np.cos(-theta_y)]
    ])
    R_after_y = Ry @ R_after_z

    # Angle to rotate around x-axis to align the y-axis and z-axis properly with the global y-axis and z-axis
    theta_x = np.arctan2(R_after_y[1, 2], R_after_y[1, 1])  # arctan2(z, y) of the second row

    # Calculated angle (converted to degrees for easier interpretation)
    # theta_x_deg = np.degrees(theta_x)

    return theta_x 
