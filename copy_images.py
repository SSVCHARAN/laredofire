#!/usr/bin/env python3
import os, glob, shutil

artifact_dir = "/home/ssvcharan/.gemini/antigravity/brain/88d6fd6c-1e39-4106-a391-8a4c283bfc8e"
dest_dir = "/home/ssvcharan/Antigravity/LaredoFire/images"

os.makedirs(dest_dir, exist_ok=True)

# Find generated images
hero_imgs = glob.glob(f"{artifact_dir}/hero_firefighter_banner_*.jpg")
mission_imgs = glob.glob(f"{artifact_dir}/mission_firefighter_gear_*.jpg")

if hero_imgs:
    latest_hero = sorted(hero_imgs)[-1]
    shutil.copy(latest_hero, f"{dest_dir}/hero_banner.jpg")
    print(f"Copied {latest_hero} -> {dest_dir}/hero_banner.jpg")

if mission_imgs:
    latest_mission = sorted(mission_imgs)[-1]
    shutil.copy(latest_mission, f"{dest_dir}/mission_gear.jpg")
    print(f"Copied {latest_mission} -> {dest_dir}/mission_gear.jpg")

