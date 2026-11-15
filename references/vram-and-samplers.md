# 显存与采样参数速查（RTX 5090 33.7 GB / 96 GB RAM）

数值来自参考实例实测与既有工作流参数，不是教科书值。显存吃紧时按「降分辨率 → 降帧数/批量 → 换量化 → block swap」顺序处理。

## 1. 显存预算

| 任务 | 配置 | 预估峰值 | 备注 |
|---|---|---|---|
| Zimage Turbo 图 | 512×768 / 720×1280，6~9 步 | 10~14 GB | 实测 512×768 含加载 48.6s |
| Krea2 Turbo 图 | 768×1024，8 步 | 12~16 GB | 实测 42.6s |
| FLUX2-Klein 9B | 1024×1024，10 步 | 16~20 GB | fp8 权重 |
| Qwen-Image 2512 | 720×1280 + SeedVR2 放大 | 18~24 GB | 放大链另算 |
| SDXL + 4x 放大 | 832×1216 → 4x | 10~14 GB | 放大后分辨率高，注意内存 |
| Wan2.2 I2V 480p | 832×480 / 81 帧 | 20~26 GB | 720p 需 block swap |
| Wan2.2 I2V 720p | 1280×720 / 81 帧 | 28~33 GB+ | wrapper + fp8 + swap 25 块起 |
| LTX2.5 视频 | 768×512 / 121~241 帧 | 24~32 GB | 带 audio VAE 更高 |
| MiniMax-H3 参考生视频 | 1344×768 / 124 帧 / 25 步 | 28~33 GB | turbo 4~8 步明显更快 |
| H3 双采/三采放大 | 上述 + latent upscaler | 30~33 GB | 用 `MiniMaxLowVRAMAttention(head_chunks=4)` |
| SeedVR2 放大 | 2048 输出 | 18~26 GB | 分块（TTP）可再降 |
| Qwen3-TTS / ACE-Step | — | 6~10 GB | — |

## 2. 模型参数（参考实例常用）

| 模型 | 步数 | CFG | 采样器 / 调度器 | 说明 |
|---|---|---|---|---|
| Zimage Turbo | 6~9 | **1** | euler / simple | 必须 cfg=1；neg 基本无效 |
| Krea2 Turbo | 8 | **1** | euler / simple | 可加风格 LoRA |
| FLUX2-Klein 9B | 10 | **1** | res_2s / bong_tangent | 取自 C12 实测配置 |
| Qwen-Image 2512 | 8（Lightning LoRA） | 1 | res_2s / beta57 | 中文提示词友好 |
| Qwen-Image 2.1 | 20 | 1 | euler / simple | 配合 `ModelSamplingFlux` |
| SDXL / Illustrious | 28~30 | 5~7 | dpmpp_2m_sde / karras | 加 `CLIPSetLastLayer(-2)` |
| Wan2.2 I2V（原生） | 25 | 6 | euler / normal | 832×480，81 帧，16fps |
| Wan2.2 + LightX2V | 4~6 | 1 | euler / normal | LoRA 加速，注意 cfg |
| LTX2.5 | 手动 sigma（8 段左右） | 1 | euler_ancestral | 手动 sigmas 链 |
| MiniMax-H3 | 25（turbo 4~8） | 1 | res_multistep / simple | 帧数 124≈5s@24fps |
| ACE-Step 音乐 | 20~30 | 5~7 | euler / simple | 与 `TextEncodeAceStepAudio1.5` 配 |
| Qwen3-TTS | — | — | — | 只需选 Base/VoiceDesign |

## 3. 采样器/调度器怎么选

| 采样器 | 特点 | 适用 |
|---|---|---|
| euler | 最快、稳定 | turbo/蒸馏模型、预览 |
| euler_ancestral | 随机性更强 | 二次元、创意 |
| res_2s | 细节好、需多步 | Qwen/FLUX2 系列（本机常用） |
| res_multistep | H3 推荐 | MiniMax-H3 |
| dpmpp_2m / dpmpp_2m_sde | 通用质量高 | SDXL 系 |
| lcm | 极低步数 | 蒸馏/LoRA |

调度器：`simple`（turbo 通用）、`beta57`/`bong_tangent`（Qwen/FLUX2）、`karras`（SDXL 低步数）、`normal`（Wan/Hunyuan）、`sgm_uniform`（SD3 系）。

## 4. 批量与变体

- 图：`EmptyLatentImage.batch_size = N` 最省事（同 seed 不同噪声由一个 batch 生成）；要**不同 seed** 时复制采样链（参考 21Pdontno 的 batch 模式），或多次 `submit --seed`。
- 视频：受显存限制，批量通常=1；用循环/多次提交。
- 对比图：`Image Comparer (rgthree)`、`ImageGrid-TY`、XY 图（`Z11`）。
