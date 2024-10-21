"""Calculates speed and acceleration vectors on PFF tracks."""

from typing import cast

from pandas import DataFrame
from tqdm import tqdm


def _compute_derivatives(df: DataFrame) -> DataFrame:
    df = df.sort_values('frame_id')

    df['time_diff'] = df['elapsed_seconds'].diff()

    df['vx'] = df['x'].diff() / df['time_diff']
    df['vy'] = df['y'].diff() / df['time_diff']
    df['ax'] = df['vx'].diff() / df['time_diff']
    df['ay'] = df['vy'].diff() / df['time_diff']
    df['speed'] = (df['vx'] ** 2 + df['vy'] ** 2) ** 0.5

    return df.drop(columns=['time_diff'])


def _compute_ball_derivatives(df: DataFrame) -> DataFrame:
    ball_df = df.drop_duplicates(subset='frame_id', keep='first')

    ball_df = ball_df[['frame_id', 'elapsed_seconds', 'ball_x', 'ball_y', 'ball_z']]
    ball_df = cast(DataFrame, ball_df)

    ball_df = ball_df.sort_values('elapsed_seconds')

    ball_df['time_diff'] = ball_df['elapsed_seconds'].diff()

    ball_df['ball_vx'] = ball_df['ball_x'].diff() / ball_df['time_diff']
    ball_df['ball_vy'] = ball_df['ball_y'].diff() / ball_df['time_diff']
    ball_df['ball_vz'] = ball_df['ball_z'].diff() / ball_df['time_diff']
    ball_df['ball_ax'] = ball_df['ball_vx'].diff() / ball_df['time_diff']
    ball_df['ball_ay'] = ball_df['ball_vy'].diff() / ball_df['time_diff']
    ball_df['ball_az'] = ball_df['ball_vz'].diff() / ball_df['time_diff']
    ball_df['ball_speed'] = (
        ball_df['ball_vx'] ** 2 + ball_df['ball_vy'] ** 2 + ball_df['ball_vz'] ** 2
    ) ** 0.5

    ball_df = ball_df[
        [
            'frame_id',
            'ball_vx',
            'ball_vy',
            'ball_vz',
            'ball_speed',
            'ball_ax',
            'ball_ay',
            'ball_az',
        ]
    ]

    return df.merge(ball_df, on='frame_id', how='left')


def add_players_speed(frames_df: DataFrame) -> DataFrame:
    tqdm.pandas(desc='Adding player speed, velocity, and acceleration in each frame')
    return (
        frames_df.groupby(['period', 'team', 'shirt'], as_index=False)
        .progress_apply(_compute_derivatives)
        .reset_index(drop=True)
    )


def add_ball_speed(frames_df: DataFrame) -> DataFrame:
    tqdm.pandas(desc='Adding ball speed, velocity, and acceleration in each frame')
    return (
        frames_df.groupby('period', as_index=False)
        .progress_apply(_compute_ball_derivatives)
        .reset_index(drop=True)
    )
