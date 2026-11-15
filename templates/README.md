# templates

这些是 `comfy.py build` 用的 **recipe**（不是最终工作流 JSON），build 后会生成带完整 slot/link/widgets 的 UI 工作流。
所有模板都已用参考实例 `.cache/object_info.json` 做过离线 build + validate；"实跑"列指是否在远端 GPU 上真跑过。

| 文件 | 用途 | 结构校验 | 远端实跑 |
|---|---|---|---|
| `zimage-t2i.json` | Zimage Turbo 文生图 512×768 / 6 步 | ✅ | ✅ 48.6s |
| `krea2-t2i.json` | Krea2 Turbo 写实人像 768×1024 / 8 步 | ✅ | ✅ 42.6s |
| `zimage-i2i.json` | Zimage 图生图（LoadImage→VAEEncode，denoise 0.55） | ✅ | ⏳ 实例离线 |
| `flux2-klein-t2i.json` | FLUX2-Klein 9B 文生图 1024×1024 / 10 步 | ✅ | ⏳ 实例离线 |
| `sdxl-illustrious-t2i.json` | SDXL Illustrious 832×1216 / 28 步 + 4x 放大 | ✅ | ⏳ 实例离线 |
| `wan22-native-i2v.json` | Wan2.2 原生节点图生视频 832×480 / 81 帧 | ✅ | ⏳ 实例离线 |

用法：

```powershell
python scripts\comfy.py build templates\zimage-t2i.json -o ..\wf.json
python scripts\comfy.py validate ..\wf.json
python scripts\comfy.py submit ..\wf.json --wait --download ..\out
```

改参数直接编辑 recipe 的 `widgets`；加节点/连线按 `references/workflow-format.md` 的 recipe 语法。
想让每个节点带中文可读标题：recipe 顶层加 `"annotate": true`，build 会生成 `[分类] 类型` 的节点标题。
