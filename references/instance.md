# 实例配置与参考实例说明

本技能不绑定任何固定主机。你需要提供一台运行 ComfyUI 的机器（本机 / 局域网 / 云 GPU 均可），
通过 SSH 隧道访问其 HTTP API。

## 1. 配置（必做）

```powershell
cd <skill 目录>
Copy-Item instance.example.json instance.json
```

编辑 `instance.json`：

```json
{
  "host": "your-gpu-box.example.com",
  "port": 22,
  "user": "root",
  "password": "your-password-or-use-env",
  "local_port": 16006,
  "remote_port": 6006
}
```

也可以用环境变量（优先级高于文件）：
`COMFY_SSH_HOST`、`COMFY_SSH_PORT`、`COMFY_SSH_USER`、`COMFY_SSH_PASSWORD`、
`COMFY_TUNNEL_PORT`、`COMFY_REMOTE_PORT`、`COMFY_BASE_URL`。

> 安全：`instance.json` 已加入 `.gitignore`，**不要**提交密码。
> 更稳妥的做法是只设环境变量，或用 SSH key（脚本目前用密码认证，key 认证可自行改 `remote.py`）。

配置好后：

```powershell
python scripts\comfy.py tunnel     # 本地 16006 -> 远端 127.0.0.1:6006
python scripts\comfy.py stats      # 应打印 ComfyUI 版本与 GPU
python scripts\comfy.py catalog    # 拉取 /object_info（节点目录）
```

如果 ComfyUI 不在远端 6006 端口，改 `remote_port`；如果它本来就监听在可直连的地址，
可以设 `COMFY_BASE_URL=http://host:port` 后跳过隧道。

## 2. 目录结构（ComfyUI 侧）

```
<ComfyUI>/
├── user/default/workflows/     # 工作流 JSON（技能交付物放这里）
├── input/                      # 上传的图片/音频/视频
├── output/                     # 生成结果
├── models/                     # 模型（可能是指向共享存储的符号链接）
└── custom_nodes/               # 自定义节点包
```

本技能默认把成品写到 `user/default/workflows/<分类>/`，测试产物在 `output/` 下。

## 3. 参考实例（技能里的事实来源）

本技能的 patterns / node-catalog / workflow-index 来自一台真实机器的实测，供对照：

| 项 | 值 |
|---|---|
| ComfyUI | 0.44.0，前端 1.58.5 |
| GPU | RTX 5090（33.7 GB VRAM），96 GB 内存 |
| 工作流 | 150 个（13 个中文分类：图像生成/编辑、Krea2、Zimage、SDXL、Wan/LTX 视频、对口型、放大、音频、动作迁移、MiniMax-H3、通用、工具） |
| 节点 | 6,619 个类型，custom_nodes 约 200 个包 |
| 模型族 | Zimage/Krea2/Qwen-Image/SDXL、Wan2.1/2.2、LTX2.3/2.5、MiniMax-H3、Qwen3-TTS、ACE-Step、SeedVR2、RTX VSR 等 |

你的机器上模型/节点不同时：`comfy.py catalog` 重新抓取，`comfy.py nodes <关键词>` 查真实可用项；
模板中的模型名按你的组合框选项替换。

## 4. 常见约定（示例实例，仅供参考）

- 文件名前缀分类：`A` 图像生成、`B` 编辑、`C` Krea2/Zimage、`E` SDXL、`G` Wan/LTX、`J` 对口型、`M` 放大、`N` 音频、`P` 动作迁移、`U` H3、`Y` 通用、`Z` 工具。
- 常用开关节点：`Any Switch`、`LazySwitch2way`、`rgthree Fast Groups Muter/Bypasser`；省连线：`SetNode/GetNode`。
- 采样两条路线：`KSampler`（单模型）与 `SamplerCustomAdvanced`（RandomNoise + Guider + Scheduler，便于二采/三采）。
- 显存吃紧：`VRAMCleanup`、block swap、`MiniMaxLowVRAMAttention`、fp8/int8 权重。
- 输出前缀常用日期占位符：`%date:yyyyMMdd%/image_`。

## 5. 实例离线 / 重启

云实例可能被回收或迁移，表现为 SSH 断开、端口不可达（`Test-NetConnection <host> -Port <port>` 返回 False）。

1. 端口仍通 → 重新 `comfy.py tunnel` 即可；
2. 不通 → 在平台重启实例，确认新的 SSH 端口/密码，更新 `instance.json`；
3. 恢复后重跑 `catalog` 刷新节点目录；
4. 离线也能干活：`.cache/object_info.json` 缓存存在时，`build`/`validate`/`convert` 不需要实例在线，
   只有 `submit`/`stats`/`catalog` 需要。

## 6. 安全与共享

- 不要提交 `instance.json`、`.cache/`、生成产物（`.gitignore` 已覆盖）。
- 共享机器：不要改 `custom_nodes` 源码、启动脚本或模型软链；只往 `user/default/workflows/` 写工作流。
- 生成内容与模型许可由使用者自行负责。
