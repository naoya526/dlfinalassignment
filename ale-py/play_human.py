import gymnasium as gym
import ale_py
import pygame
import numpy as np

# ALE環境を登録
gym.register_envs(ale_py)

# Breakout環境を作成（画面描画なし）
env = gym.make("ALE/Breakout-v5", render_mode="rgb_array")
state, info = env.reset()

# pygameの初期化
pygame.init()
scale = 4  # 倍率（画面サイズ調整用）
width, height = 160 * scale, 210 * scale
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Breakout - Human Play")
clock = pygame.time.Clock()

# ゲームループ
done = False
action = 0  # 初期アクションはNOOP

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                action = 3  # MOVE_LEFT
            elif event.key == pygame.K_RIGHT:
                action = 2  # MOVE_RIGHT
            elif event.key == pygame.K_SPACE:
                action = 1  # FIRE
        elif event.type == pygame.KEYUP:
            action = 0  # NOOP（キーを離したら）

    state, reward, terminated, truncated, info = env.step(action)
    done = terminated or truncated

    # フレームをpygame用に描画
    frame = np.transpose(state, (1, 0, 2))  # 軸を並び替え
    surface = pygame.surfarray.make_surface(frame)
    surface = pygame.transform.scale(surface, (width, height))
    screen.blit(surface, (0, 0))
    pygame.display.flip()

    clock.tick(30)  # FPS制限（30）

# 終了処理
pygame.quit()
env.close()
