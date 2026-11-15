> 说明：本索引来自**参考实例**（一台真实机器），仅含工作流文件名与节点链，不含提示词正文；在你的实例上文件名/分类可能不同，按需替换即可。

# 既有工作流索引（150 个，均在本机远程实例）

来源：/root/ComfyUI/user/default/workflows/（导出时间 2026-11-15）。
每行：**文件名**（节点数）— 按执行顺序去噪后的主要节点链（省略 Note/Reroute/Label/Set/Get 等辅助节点）。
缩进行是引用到的关键权重文件。

用法：
- 找同类参考 → 按分类浏览，挑最接近的 1-2 个；
- 直接复用 → python scripts/remote.py get /root/ComfyUI/user/default/workflows/<分类>/<文件>.json .
ef.json，然后按需改控件；
- 想看某个工作流的完整节点清单 → 下载后用 python scripts/comfy.py convert ref.json（会先 validate）或本地 python 打印 widgets_values_named。

# 工作流清单


## (root)

- **通用反推** (8 nodes) — llama_cpp_parameters → LoadImage → llama_cpp_model_loader → llama_cpp_instruct_adv

## A图像-生成

- **A01-文生图-Qwen2512高清放大** (21 nodes) — SeedVR2LoadDiTModel → SeedVR2LoadVAEModel → CLIPLoader → VAELoader → UNETLoader → INTConstant → CLIPTextEncode → LoraLoaderModelOnly → CR SDXL Aspect Ratio → KSampler → VAEDecode → ImageScaleBy → SeedVR2VideoUpscaler → LayerColor: AutoAdjustV2
  - weights: Qwen/Kook_Qwen_V3极致真实.safetensors, Qwen/Kook_Qwen_真实幻想V2.safetensors, Qwen/Qwen-Image-2512-Lightning-4steps-V1.0-fp32.safetensors, qwen/qwen_image_2512_fp8_e4m3fn.safetensors
- **A08-洗图-Qwen二次元转真人高清放大** (59 nodes) — VAELoader → ControlNetLoader → Text Multiline → SeedVR2LoadVAEModel → UNETLoader → CLIPLoader → LoadImage → SeedVR2LoadDiTModel → ZealmanLLM_ModelLoader → SetUnionControlNetType → VAEEncode → ImageScaleToTotalPixels → TextEncodeQwenImageEdit → LoraLoaderModelOnly
  - weights: Qwen/AnythingtoRealCharacters2511_20.safetensors, Qwen/BJD娃娃V2.0_04.safetensors, Qwen/Qwen-Image-Edit-2511-Lightning-8steps-V1.0-bf16.safetensors, Qwen/Qwen动漫转写实真人V2_V2.safetensors
- **C01-文生图-Zimage基础版** (15 nodes) — CLIPLoader → VAELoader → easy promptList → EmptyLatentImage → UNETLoader → LoraLoaderModelOnly → CLIPTextEncode → ConditioningZeroOut → KSampler → VAEDecode → SaveImage
  - weights: Zimage/AWPortrait-Z.safetensors, Zimage/z_image_turbo_bf16.safetensors, euler, qwen_3_4b.safetensors
- **C08-图像黑兽DarkBeast-ZiT-V8-UltraSimple-Workflow-ComfyUI** (22 nodes) — VAELoader → EmptySD3LatentImage → CLIPLoader → UNETLoader → CLIPTextEncode → LoraLoaderModelOnly → ConditioningZeroOut → ModelSamplingAuraFlow → KSampler → VAEDecode → SaveImage → ImageScaleBy → VAEEncode
  - weights: Flux/DarkKlein9b_v2BFS_extracted_lora_r256.safetensors, Zimage/ZIT-手脚身体皮肤v1.1.safetensors, Zimage/darkBeastMar1526Latest_darkblitz6Beyondnsfw.safetensors, ae.safetensors
- **C09-图像黑兽DarkBeast-ZIT-Klein-V8-Hybrid-Workflow-ComfyUI** (54 nodes) — KSamplerSelect → SeedVR2LoadDiTModel → SeedVR2LoadVAEModel → CLIPLoader → VAELoader → LoadImage → EmptyLatentImage → PrimitiveInt → String → UNETLoader → CLIPTextEncode → RandomNoise → LoraLoaderModelOnly → ConditioningZeroOut
  - weights: Flux/DarkKlein9b_v2BFS_extracted_lora_r256.safetensors, Zimage/darkBeastMar1526Latest_darkblitz6Beyondnsfw.safetensors, ae.safetensors, euler
- **C10-图像Moody-Zimage-Simple-Workflow-V4** (54 nodes) — CLIPLoader → UltralyticsDetectorProvider → SAMLoader → SeedVR2LoadVAEModel → SeedVR2LoadDiTModel → UpscaleModelLoader → EmptyLatentImage → UNETLoader → VAELoader → FloatConstant → PrimitiveInt → Power Lora Loader (rgthree) → SimpleMath+ → ModelSamplingAuraFlow
  - weights: 4x-UltraSharp.pth, 4x_NMKD-Superscale-SP_178000_G.pth, Zimage/moodyRealMix_zitV4DPO.safetensors, ae.safetensors
- **C12-瑶光-动漫-MJ风格工作流** (71 nodes) — SeedVR2LoadVAEModel → SeedVR2LoadDiTModel → KSamplerSelect → VAELoader → CLIPLoader → CR Prompt Text → easy promptLine → Fast Groups Muter (rgthree) → TTResolutionSelector → UNETLoader → Note Plus (mtb) → CheckpointLoaderSimple → CR Text Concatenate → RandomNoise
  - weights: Flux/Klein-yizhixing-lora.safetensors, euler, flux/flux-2-klein-9b-fp8.safetensors, flux2-vae.safetensors
- **C13-kinghere-Z-image-动漫-小说-造影** (32 nodes) — EmptyLatentImage → LoadImage → ModelPatchLoader → CheckpointLoaderSimple → ImageScaleToTotalPixels → Qwen3_VQA → AIO_Preprocessor → ImpactSwitch → easy cleanGpuUsed → CLIPTextEncode → QwenImageDiffsynthControlnet → PreviewImage → ConditioningZeroOut → KSamplerAdvanced
  - weights: dpmpp_3m_sde, er_sde, kinghere-Z-image-动漫-小说-造影V3-nswf.safetensors
- **C15-Z-ImageBase-Turbo双重采样洗图工作流** (113 nodes) — SeedVR2LoadVAEModel → Int → VAELoader → CLIPLoaderGGUF → UNETLoader → INTConstant → SeedVR2LoadDiTModel → ModelPatchLoader → Fast Groups Bypasser (rgthree) → LoadImage → llama_cpp_parameters → llama_cpp_model_loader → Power Lora Loader (rgthree) → Any Switch (rgthree)
  - weights: Qwen3-4b-Z-Image-Engineer-V4-Q8_0.gguf, Zimage/ZIT-Remix-Reality-v20.safetensors, Zimage/z_image_bf16.safetensors, ae.safetensors
- **C17-Z-image瑜伽服小姐姐** (24 nodes) — CLIPLoader → VAELoader → CR Text → EmptyLatentImage → Fast Groups Bypasser (rgthree) → UNETLoader → llama_cpp_parameters → llama_cpp_model_loader → CR Text Replace → Power Lora Loader (rgthree) → llama_cpp_instruct_adv → ModelSamplingAuraFlow → TextToList → CLIPTextEncode
- **C18-豹豹喵呜制作-白玉AIO三采超高清写真生成** (62 nodes) — CheckpointLoaderSimple → UNETLoader → CLIPLoader → VAELoader → CR Text → FloatConstant → CR Seed → Fast Groups Bypasser (rgthree) → LoadImage → llama_cpp_parameters → llama_cpp_model_loader → CR Prompt Text → WJILatentPreset → Lora Loader Stack (rgthree)
- **C19-人物设定三视图zimage双采** (27 nodes) — EmptyLatentImage → CheckpointLoaderSimple → UNETLoader → SeedVR2LoadVAEModel → SeedVR2LoadDiTModel → CR Prompt Text → llama_cpp_parameters → llama_cpp_model_loader → llama_cpp_instruct_adv → TextConcatenator → CLIPTextEncode → ConditioningZeroOut → KSampler → KSamplerAdvanced
- **MOSS-Image-生图流-黑鹤** (27 nodes) — CLIPLoader → VAELoader → ResolutionSelector → UNETLoader → Fast Groups Bypasser (rgthree) → CLIPTextEncode → EmptyLatentImage → LoraLoaderModelOnly → KSampler → VAEDecode → SaveImage
  - weights: euler, flux2-vae.safetensors, moss/Moss-8stepslora_latest.safetensors, moss/moss_image_sft_int8_convrot.safetensors

## B图像-编辑

- **B01-RAW画质重建Adonis_Workflow** (32 nodes) — LoadImage → SharkOptions_Beta → VAELoader → CLIPLoader → UNETLoader → Fast Groups Bypasser (rgthree) → PrimitiveStringMultiline → easy seed → INTConstant → ImageScaleToTotalPixelsX → CLIPTextEncode → LoraLoaderModelOnly → VAEEncode → PreviewImage
- **B18-Qwen-Image-2.1基础版** (16 nodes) — CLIPLoader → UNETLoader → VAELoader → ResolutionSelector → LoadImage → ModelAttentionBackend → EmptyLatentImage → TextEncodeQwenImage21 → QwenImage21Cache → ModelSamplingFlux → KSampler → VAEDecode → SaveImageAdvanced
  - weights: euler, qwen/qwen_image_2.1_int8_convrot.safetensors, qwen3vl_8b_int8_convrot.safetensors, qwen_image_2.1_vae_bf16.safetensors
- **B19-Qwen-Image-2.1提示词优化clip版** (7 nodes) — ResolutionSelector → c291ceec-b98f-4751-9d0b-7bc288f27b30 → SaveImageAdvanced
  - weights: qwen/qwen_image_2.1_int8_convrot.safetensors, qwen3vl_8b_fp8_scaled.safetensors, qwen_image_2.1_vae_bf16.safetensors
- **B20-Qwen-Image-2.1-Turbo高速编辑版** (11 nodes) — KSamplerSelect → ManualSigmas → LoadImage → 6afdfe0f-148e-4a7f-b1bf-3922718f59a7 → TextEncodeQwenImage21 → SamplerCustom → VAEDecode → SaveImage
  - weights: euler

## C图像-Krea2

- **T01-Krea2文生图超强写实质感** (15 nodes) — VAELoader → ResolutionSelector → CLIPLoader → UNETLoader → EmptyLatentImage → CLIPTextEncode → LoraLoaderModelOnly → ConditioningZeroOut → KSampler → VAEDecode → SaveImage
- **T03-Krea2三采流-全自动文生图全模式** (50 nodes) — KSamplerSelect → RandomNoise → VAELoader → UNETLoader → Int → INTConstant → CLIPLoader → CR Prompt Text → llama_cpp_parameters → llama_cpp_model_loader → EmptyLatentImage → ModelSamplingAuraFlow → CLIPTextEncode → llama_cpp_instruct_adv
- **T04-Krea2-int8-角色设定三视图** (41 nodes) — CLIPLoader → VAELoader → EmptyLatentImage → TTResolutionSelector → CR Prompt Text → UNETLoader → ZealmanLLM_ModelLoader → RandomNoise → KSamplerSelect → CLIPTextEncode → ZealmanLLM_Generate → LoraLoaderModelOnly → ConditioningZeroOut → KSampler
  - weights: euler, flux/flux-2-klein-9b-kv_int8_convrot.safetensors, flux2-vae.safetensors, krea2/krea2-Cc风情万种-人像.safetensors
- **T05-krea2-leggings-瑜伽裤小姐姐-美学文生图** (50 nodes) — CLIPLoader → UNETLoader → VAELoader → RandomNoise → KSamplerSelect → CR Text → UpscaleModelLoader → llama_cpp_parameters → llama_cpp_model_loader → EmptyLatentImage → CLIPTextEncode → LoraLoaderModelOnly → CR Text Replace → LayerUtility: PurgeVRAM V2
  - weights: 1x-ITF-SkinDiffDetail-Lite-v1.pth, euler, f2k_9B_lcs_consist_20260415.safetensors, flux/Flux2-Klein-9B-True-v2-bf16.safetensors
- **T06-krea2-klein-包臀裙小姐姐** (57 nodes) — VAELoader → CLIPLoader → KSamplerSelect → RandomNoise → llama_cpp_parameters → UpscaleModelLoader → CR Prompt Text → UNETLoader → ResolutionSelector → String → llama_cpp_model_loader → LoraLoaderModelOnly → EmptyLatentImage → llama_cpp_instruct_adv
- **T07-Krea2图像编辑krea2edit版单图双图** (18 nodes) — ResolutionSelector → LoadImage → CLIPLoader → VAELoader → UNETLoader → EmptySD3LatentImage → LoraLoaderModelOnly → SaveImage → KSampler → VAEDecode → VAEEncode → ResizeImageMaskNode → Krea2EditModelPatch → Krea2EditGroundedEncode
- **T09-Krea2-Remix-RealCosplay-多功能合集工作流** (100 nodes) — CLIPLoader → UNETLoader → VAELoader → LoadImage → Fast Groups Bypasser (rgthree) → EmptyLatentImage → PromptExpand → SeedVR2LoadVAEModel → SeedVR2LoadDiTModel → PainterVRAM → LayerUtility: ImageScaleByAspectRatio V2 → CLIPTextEncode → Krea2ControlLoRALoader → Any Switch (rgthree)
  - weights: Krea2/Krea2_Remix_RealCosplay_rank64_v1.safetensors, Krea2\depth-control-lora.safetensors, er_sde, euler
- **T10-Krea2做剧图像4视图** (24 nodes) — CLIPLoader → VAELoader → UNETLoader → LoadImage → EmptySD3LatentImage → LoraLoaderModelOnly → ImageResizeKJv2 → VAEEncode → GetImageSize → Krea2EditGroundedEncode → Krea2EditModelPatch → KSampler → VAEDecode → SaveImage
  - weights: euler, krea/krea2_turbo_int8_convrot.safetensors, krea2/krea2_4panel.safetensors, qwen3vl_4b_fp8_scaled.safetensors
- **T11-DarkBeast-黑兽H3单采DirectorEdition短剧生产** (29 nodes) — VAELoader → UpscaleModelLoader → CR Prompt Text → WJILatentPreset → ZealmanLLM_ModelLoader → UNETLoader → CLIPLoader → Fast Groups Bypasser (rgthree) → ComfyMathExpression → ZealmanLLM_Generate → CLIPTextEncode → ConditioningZeroOut → KSampler → VAEDecode
  - weights: 4x_foolhardy_Remacri.pth, euler, krea2/darkBeastH3Director_darkBeast330.safetensors, qwen3vl_4b_bf16.safetensors
- **T13-RedCraft-Krea2-DUAL-MASO-Edition** (38 nodes) — ResolutionSelector → UNETLoader → CLIPLoader → EmptyLatentImage → VAELoader → KSamplerSelect → ManualSigmas → PrimitiveStringMultiline → Seed Generator (Image Saver) → LoraLoaderModelOnly → CLIPTextEncode → Power Lora Loader (rgthree) → ConditioningZeroOut → SamplerCustom
  - weights: er_sde, krea2/RedCraft-LowNoise-MASO-MangaDrama-Krea2Turbo-RedMix-v4.safetensors, krea2/krea2_turbo_lora_rank_64_bf16.safetensors, qwen3vl_4b_bf16.safetensors
- **T14-Krea2-Zimage双娇真实皮肤质感** (10 nodes) — ResolutionSelector → b0e5ca93-2731-42b9-8e0a-d28ea851ff81 → SaveImage → a18bf035-11cc-4a97-934b-2e85cb5c9fa6 → ImageCompare
  - weights: Zimage/z_image_turbo_int8_convrot.safetensors, ae.safetensors, qwen_3_4b.safetensors
- **T15-krea2-MJ风格工作流-在下鱼酥** (21 nodes) — CLIPLoader → UNETLoader → VAELoader → ResolutionSelector → CR Prompt Text → LoraLoaderModelOnly → EmptyLatentImage → CLIPTextEncode → ConditioningZeroOut → KSampler → VAEDecode → SaveImage
  - weights: euler, krea/krea2_turbo_int8_convrot.safetensors, krea2/alternative_reality_v1p.safetensors, krea2/babegenerator.ink-realism_helper.safetensors
- **T16-krea2-MJ风格工作流V4-在下鱼酥** (102 nodes) — ResolutionSelector → VAELoader → UNETLoader → CLIPLoader → PrimitiveStringMultiline → LoadImage → PrimitiveBoolean → Fast Groups Muter (rgthree) → PrimitiveFloat → PrimitiveInt → CLIPTextEncode → LoraLoaderModelOnly → VAEEncode → EmptyLatentImage
  - weights: depth_anything_v2_vitl.pth, er_sde, euler, flux2-vae.safetensors

## C图像-Zimage

- **C14-黑鹤001-ZITB-F2K-高清修复整合流** (259 nodes) — VAELoader → INTConstant → CLIPLoader → UpscaleModelLoader → LoadImage → EmptyLatentImage → EmptyFlux2LatentImage → Fast Groups Bypasser (rgthree) → CR Prompt Text → PrimitiveFloat → KSamplerSelect → CheckpointLoaderSimple → UNETLoader → CLIPTextEncode
  - weights: 4x-UltraSharp.pth, Flux/F2K_9b-万物转动漫AnythingtoAnime.safetensors, Flux/F2K_9b-破KLEIN-Unchained-V2.safetensors, SDXL/IL-perfectionRealisticILXL_33.safetensors

## E图像-SDXL-IL

- **4K直出hshiAnima基础工作流** (60 nodes) — CLIPLoader → VAELoader → UNETLoader → EmptyLatentImage → RandomNoise → KSamplerSelect → SeedVR2LoadVAEModel → SeedVR2LoadDiTModel → Text Load Line From File → Fast Groups Muter (rgthree) → PrimitiveStringMultiline → Power Lora Loader (rgthree) → LatentUpscaleBy → LoraLoaderModelOnly
  - weights: Flux/f2k_9B_小志一致性(0.5-0.7)lcs_consist_0412预览版preview.safetensors, anima/hsAnima_v10.safetensors, er_sde, euler
- **E01-文生图-Illustrious** (17 nodes) — EmptyLatentImage → UpscaleModelLoader → CheckpointLoaderSimple → LoraLoaderModelOnly → CLIPSetLastLayer → CLIPTextEncode → KSampler → VAEDecode → ImageUpscaleWithModelBatched → SaveImage
- **E02-文生图-SDXL-SmoothWorkflow** (24 nodes) — mxSlider2D → Text Multiline → VAELoader → SAMLoader → UltralyticsDetectorProvider → Sampler Scheduler Settings (JPS) → Int → Cfg Literal → easy seed → CheckpointLoaderSimple → EmptyLatentImage → ImpactWildcardEncode → CLIPSetLastLayer → BNK_CLIPTextEncodeAdvanced
- **E03-文生图-二次元漫画模型** (27 nodes) — VAEEncode → ImageUpscaleWithModel → PreviewImage → VAEDecode → UpscaleModelLoader → CR Text Concatenate → EmptyLatentImage → CLIPTextEncode → CR Prompt Text → KSampler → CheckpointLoaderSimple → LoadImage → WD14Tagger|pysssss → Fast Groups Bypasser (rgthree)
- **E04-Anima-琉璃AIO-豹豹喵呜** (15 nodes) — EmptySD3LatentImage → PrimitiveString → easy positive → AnimaBoosterCheckpointLoader → JoinStrings → AnimaTeaCache → easy showAnything → CLIPTextEncode → ConditioningZeroOut → KSampler → VAEDecode → SaveImage
  - weights: Amina-12steps-liuli-AIO-0_1.safetensors, er_sde

## G视频-Wan-Ltx

- **G01-图生视频-Wan2.2万相基础版** (34 nodes) — Text Multiline → WanVideoVAELoader → LoadWanVideoT5TextEncoder → WanVideoBlockSwap → Int → ImpactInt → easy int → WanVideoLoraSelect → LoadImage → WanVideoTextEncode → WanVideoModelLoader → MathExpression|pysssss → CreateCFGScheduleFloatList → LayerUtility: ImageScaleByAspectRatio V2
- **G01-图生视频-Wan2.2优化版** (40 nodes) — WanVideoTorchCompileSettings → WanVideoVAELoader → INTConstant → WanVideoLoraSelect → LoadWanVideoT5TextEncoder → WanVideoBlockSwap → LoadImage → WanVideoTextEncode → Int → WanVideoModelLoader → CreateCFGScheduleFloatList → ImageResizeKJv2 → SimpleMath+ → WanVideoSetBlockSwap
- **G02-首尾帧-Wan2.2首尾帧视频** (42 nodes) — WanVideoVAELoader → CogVideoEnhanceAVideo → WanVideoSLG → WanVideoTorchCompileSettings → WanVideoBlockSwap → easy int → Int → LoadImage → WanVideoLoraSelect → LoadWanVideoT5TextEncoder → LoadWanVideoClipTextEncoder → ImpactInt → easy seed → Text Multiline
- **G03-图生视频-Wan2.2SmoothMix** (23 nodes) — llama_cpp_model_loader → llama_cpp_parameters → INTConstant → Fast Groups Muter (rgthree) → PrimitiveStringMultiline → 1be6b577-03ed-4fa7-9a0f-ed3c147d5cc2 → LoadImage → llama_cpp_instruct_adv → KSamplerAdvanced → VHS_VideoCombine → SaveImage → abe8cce3-d580-4218-9824-5219fa585f95
- **G04-图生视频-Wan2.2SmoothMix图生** (49 nodes) — VAELoader → CLIPLoader → DownloadAndLoadFlorence2Model → CLIPVisionLoader → INTConstant → LoadImage → UNETLoader → CLIPTextEncode → MathExpression|pysssss → LayerUtility: ImageScaleByAspectRatio V2 → Florence2Run → PathchSageAttentionKJ → CLIPVisionEncode → ImageResizeKJv2
- **G05-图生视频-Wan2.2-LightX2V最强动态** (54 nodes) — INTConstant → CLIPVisionLoader → Wan22PromptSelector → VAELoader → CR Text → UNETLoader → CLIPLoader → LoadImage → CLIPTextEncode → MathExpression|pysssss → Text Concatenate → LoraLoaderModelOnly → LayerUtility: ImageScaleByAspectRatio V2 → CLIPVisionEncode
- **G06-首尾帧-Wan2.2-LightX2V超动感** (67 nodes) — INTConstant → LoadImage → UNETLoader → CLIPLoader → VAELoader → CLIPVisionLoader → llama_cpp_parameters → llama_cpp_model_loader → ModelSamplingSD3 → WanVideoNAG → CLIPTextEncode → CLIPVisionEncode → ImageResizeKJv2 → LoraLoaderModelOnly
- **G07-图生视频-Wan2.2-LightX2V-WorkFisher** (79 nodes) — VAELoader → CLIPLoader → INTConstant → Int → LoadImage → UNETLoader → llama_cpp_parameters → llama_cpp_model_loader → MathExpression|pysssss → llama_cpp_instruct_adv → CLIPTextEncode → wanBlockSwap → LoraLoaderModelOnly → LayerUtility: ImageScaleByAspectRatio V2
- **G10-图生视频-Wan2.2SmoothMixV2** (44 nodes) — UNETLoader → CLIPLoader → VAELoader → LoadImage → CLIPVisionLoader → INTConstant → llama_cpp_model_loader → llama_cpp_parameters → PrimitiveStringMultiline → LoraLoaderModelOnly → CLIPTextEncode → CLIPVisionEncode → MathExpression|pysssss → llama_cpp_instruct_adv
- **H42-韩国UP-LTX2.3MultiImageReference** (111 nodes) — CheckpointLoaderSimple → KSamplerSelect → RandomNoise → LatentUpscaleModelLoader → LTXAVTextEncoderLoader → ManualSigmas → PrimitiveFloat → Fast Groups Bypasser (rgthree) → INTConstant → TTResolutionSelector → LTXVAudioVAELoader → Power Lora Loader (rgthree) → CLIPTextEncode → CM_FloatToInt
- **H50-LTX2.5文生视频** (49 nodes) — PrimitiveBoolean → CLIPLoader → ResolutionSelector → UNETLoader → PrimitiveStringMultiline → PrimitiveInt → VAELoader → ManualSigmas → RandomNoise → LatentUpscaleModelLoader → KSamplerSelect → TextGenerateLTX2Prompt → CLIPTextEncode → ComfyMathExpression
  - weights: Ltx/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors, euler_ancestral, gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors, ltx-2.5-audio-vae-bf16.safetensors
- **H51-LTX2.5图生视频** (57 nodes) — LoadImage → ResolutionSelector → CLIPLoader → PrimitiveBoolean → PrimitiveStringMultiline → PrimitiveInt → KSamplerSelect → RandomNoise → ManualSigmas → LatentUpscaleModelLoader → UNETLoader → VAELoader → ResizeImageMaskNode → CLIPTextEncode
  - weights: Ltx/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors, euler_ancestral, gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors, ltx-2.5-audio-vae-bf16.safetensors
- **H52-LTX2.5首尾帧视频** (48 nodes) — LoadImage → ManualSigmas → SamplerEulerAncestral → RandomNoise → UNETLoader → VAELoader → CLIPLoader → PrimitiveBoolean → PrimitiveInt → PrimitiveStringMultiline → CLIPTextEncode → ResizeImageMaskNode → ComfyMathExpression → GetImageSize
  - weights: Ltx/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors, gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors, ltx-2.5-audio-vae-bf16.safetensors, ltx-2.5-video-vae-bf16.safetensors
- **H54-LTX2.5视频超分V1** (39 nodes) — VAELoaderKJ → KSamplerSelect → CLIPLoader → ManualSigmas → Text String → OTUNetLoaderW8A8 → LatentUpscaleModelLoader → VAELoader → VHS_LoadVideo → RandomNoise → CLIPTextEncode → CR Text Input Switch (4 way) → LTX2MemoryEfficientSageAttentionPatch → VHS_SplitImages
  - weights: Ltx/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors, gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors, lcm, ltx-2.5-audio-vae-bf16.safetensors

## J视频-对口型数字人

- **J03-对口型-InfiniteTalk官方流长视频无衰减** (134 nodes) — INTConstant → CLIPLoader → VAELoader → ModelPatchLoader → LoadImage → AudioEncoderLoader → LoadAudio → CLIPVisionLoader → UNETLoader → CLIPTextEncode → WanInfiniteTalkToVideo → AudioCrop → CLIPVisionEncode → ModelSamplingSD3
- **J04-对口型-InfiniteTalk单人图像驱动** (55 nodes) — CLIPVisionLoader → LoadWanVideoT5TextEncoder → DownloadAndLoadWav2VecModel → LoadAudio → LoadImage → WanVideoLoraSelect → WanVideoVAELoader → WanVideoBlockSwap → MultiTalkModelLoader → easy int → WanVideoTextEncode → AudioCrop → AudioSeparation → Audio Duration (mtb)
  - weights: Wan2_1_VAE_bf16.safetensors, clip_vision_h.safetensors, umt5-xxl-enc-fp8_e4m3fn.safetensors
- **J05-对口型-InfiniteTalk单人视频驱动** (63 nodes) — WanVideoTorchCompileSettings → CLIPVisionLoader → LoadWanVideoT5TextEncoder → WanVideoLoraSelect → easy int → MultiTalkModelLoader → DownloadAndLoadWav2VecModel → LoadAudio → WanVideoBlockSwap → VHS_LoadVideo → WanVideoVAELoader → WanVideoTextEncode → AudioCrop → LayerUtility: ImageScaleByAspectRatio V2
- **J06-对口型-InfiniteTalk双人图像驱动** (68 nodes) — LoadAudio → DownloadAndLoadWav2VecModel → LoadWanVideoT5TextEncoder → CLIPVisionLoader → easy int → LoadImage → WanVideoLoraSelect → WanVideoVAELoader → WanVideoBlockSwap → MultiTalkModelLoader → AudioCrop → WanVideoTextEncode → 2b077f36-1f1b-4db1-b4ee-eac6e2ffb2f5 → AudioSeparation
- **J08-LTX2.3数字人说话唱歌对口型-优化升级kj版** (115 nodes) — KSamplerSelect → VAELoader → VAELoaderKJ → INTConstant → DualCLIPLoader → PrimitiveStringMultiline → UNETLoader → PrimitiveFloat → MelBandRoFormerModelLoader → LoadAudio → LatentUpscaleModelLoader → LoadImage → SolidMask → RandomNoise
- **J09-LTX2.3双人对话-图生视频音画同步-KJ优化版** (66 nodes) — VAELoader → VAELoaderKJ → DualCLIPLoader → KSamplerSelect → PrimitiveStringMultiline → UNETLoader → PrimitiveInt → LoadImage → Int → easy positive → llama_cpp_parameters → llama_cpp_model_loader → CR Prompt Text → CLIPTextEncode
- **J15-LTX2.3数字人文生图生自由切换版-爱屋** (60 nodes) — KSamplerSelect → LTXAVTextEncoderLoader → LTXVAudioVAELoader → RandomNoise → CheckpointLoaderSimple → LatentUpscaleModelLoader → LoadImage → PrimitiveBoolean → VHS_LoadAudioUpload → CLIPTextEncode → BasicScheduler → PathchSageAttentionKJ → ResizeImagesByLongerEdge → LTXVAudioVAEEncode
  - weights: euler, ltx-2.3-22b-dev.safetensors, ltx-2.3-22b-distilled-1.1.safetensors, ltx-2.3-spatial-upscaler-x2-1.1.safetensors
- **J16-LTX2.5数字人口播** (58 nodes) — PrimitiveInt → RandomNoise → ManualSigmas → PrimitiveBoolean → UNETLoader → CLIPLoader → LatentUpscaleModelLoader → VAELoader → KSamplerSelect → PrimitiveStringMultiline → LoadImage → VHS_LoadAudioUpload → CR Prompt Text → WJILatentPreset
  - weights: Ltx/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors, euler_ancestral, gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors, ltx-2.5-audio-vae-bf16.safetensors

## M高清放大去水印

- **M02-放大-SeedVR2-TTP高清放大** (19 nodes) — SeedVR2TorchCompileSettings → INTConstant → LoadImage → SeedVR2LoadDiTModel → SeedVR2LoadVAEModel → MathExpression|pysssss → LayerUtility: ImageScaleByAspectRatio V2 → TTP_Tile_image_size → TTP_Image_Tile_Batch → ImpactImageBatchToImageList → easy imageSizeBySide → SeedVR2VideoUpscaler → ImageListToImageBatch → TTP_Image_Assy
- **M07-NVIDA-RTX高清放大** (6 nodes) — LoadImage → RTXVideoSuperResolution → PreviewImage
- **M15-FlashVSR视频超分** (16 nodes) — VHS_LoadVideo → FlashVSRInitPipe → INTConstant → LayerUtility: ImageScaleByAspectRatio V2 → VHS_VideoInfo → FlashVSRNodeAdv → VHS_VideoCombine
- **M16-LTX2.5放大视频** (34 nodes) — UNETLoader → VAELoader → CLIPLoader → LatentUpscaleModelLoader → VHS_LoadVideo → RandomNoise → KSamplerSelect → LoadImage → PrimitiveFloat → LoraLoaderModelOnly → CLIPTextEncode → VAEEncode → LTXVAudioVAEEncode → RepeatImageBatch
  - weights: Ltx/ltx-2.3-22b-ic-lora-ingredients-0.9.safetensors, Ltx/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors, euler_ancestral, gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors
- **M17-RTX插帧视频超分** (13 nodes) — VHS_LoadVideo → Float → RIFEInterpolation → RTXVideoSuperResolution → VHS_VideoCombine
  - weights: flownet.pkl
- **M18-VOSR图片视频超分-模糊变高清** (20 nodes) — VOSR2ModelLoader → Fast Groups Muter (rgthree) → LoadImage → LoadVideo → VOSR2Upscale → GetVideoComponents → SaveImage → JWImageResizeByLongerSide → easy imageSize → RTXVideoSuperResolution → VHS_VideoCombine
- **M19-LTX2.5视频去字幕** (34 nodes) — VHS_LoadVideo → VAELoader → UNETLoader → CLIPLoader → RandomNoise → KSamplerSelect → ManualSigmas → CR Text → ResizeImageMaskNode → VHS_VideoInfoLoaded → LoraLoaderModelOnly → CLIPTextEncode → easy imageSize → GetImageRangeFromBatch
  - weights: Ltx/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors, Ltx/ltx2.3-ic-subtitles-remove-general.safetensors, Ltx/ltx2.3-ic-watermark-remove-general.safetensors, euler_ancestral_cfg_pp
- **M20-RelayVSR视频高速超分** (13 nodes) — LoadVideo → UNETLoader → VAELoader → GetVideoComponents → RelayVSRConditioning → KSampler → VSRDecode → ZealmanVideoOutput
  - weights: RelayVSR/relayvsr_x2_int8_convrot.safetensors, euler, relayvsr_flash_vae_x2_fp32.safetensors

## N声音生成-音乐生成-声音克隆

- **N01-多人声音克隆FishAudioS2pro** (23 nodes) — LoadImage → LoadAudio → Fast Groups Bypasser (rgthree) → FishS2TTS → Apply Whisper → SaveAudio → FishS2VoiceCloneTTS → FishS2MultiSpeakerTTS
- **N02-单人声音克隆FishAudioS2pro** (8 nodes) — LoadAudio → CR Prompt Text → Apply Whisper → FishS2VoiceCloneTTS → SaveAudio
- **N03-双人声音克隆FishAudioS2pro** (13 nodes) — LoadAudio → CR Text → Apply Whisper → easy showAnything → FishS2MultiSpeakerTTS → SaveAudio
- **N04-mmaudio** (11 nodes) — MMAudioFeatureUtilsLoader → VHS_LoadVideo → MMAudioModelLoader → VHS_VideoInfo → MMAudioSampler → PreviewAudio → VHS_VideoCombine
- **N05-黑鹤001-ACE-Step-音乐歌曲生成流** (18 nodes) — UNETLoader → DualCLIPLoader → VAELoader → PrimitiveInt → Fast Groups Bypasser (rgthree) → EmptyAceStep1.5LatentAudio → ModelSamplingAuraFlow → TextEncodeAceStepAudio1.5 → ConditioningZeroOut → KSampler → VAEDecodeAudio → SaveAudioMP3
  - weights: ace_1.5_vae.safetensors, acestep/acestep_v1.5_xl_turbo_bf16.safetensors, euler
- **N06-Qwen3TTS音频克隆** (11 nodes) — LoadAudio → CR Prompt Text → TDQwen3TTSModelLoader → Apply Whisper → TDQwen3TTSVoiceClone → PreviewAny → SaveAudio
- **N06-Qwen3TTS音频创造** (8 nodes) — CR Prompt Text → TDQwen3TTSModelLoader → TDQwen3TTSVoiceDesign → SaveAudio
- **N07-stable-audio-3-medium** (30 nodes) — CLIPLoader → CR Text → CheckpointLoaderSimple → PrimitiveFloat → PrimitiveStringMultiline → PrimitiveBoolean → Int → CLIPTextEncode → EmptyLatentAudio → ComfyMathExpression → easy anythingIndexSwitch → PreviewAny → StringReplace → TextGenerate
  - weights: lcm, qwen3.5_4b_bf16.safetensors, stable-audio-3/stable_audio_3_medium.safetensors, t5gemma_b_b_ul2.safetensors
- **N08-MiniMax_Music3基础工作流** (16 nodes) — VAELoader → UNETLoader → CLIPLoader → SeedNode → MiniMaxMusic3TextEncode → ConditioningZeroOut → EmptyMiniMaxMusic3LatentAudio → KSampler → VAEDecodeAudioTiled → VAEDecodeAudio → SaveAudioAdvanced
- **N09-yue2-音乐生成-支持翻唱-神棍** (23 nodes) — CheckpointLoaderSimple → PrimitiveStringMultiline → AudioEncoderLoader → LoadAudio → Fast Groups Muter (rgthree) → SheetSage2AudioToABC → YuE2GenerateABC → Any Switch (rgthree) → PreviewAny → YuE2GenerateMusic → EmptyYuE2LatentAudio → KSampler → VAEDecodeAudio → VAEDecodeAudioTiled
  - weights: dpm_2, yue2_3b_bf16.safetensors

## P视频-动作迁移

- **P02-动作迁移-Wan2.2Animate角色迁移** (40 nodes) — INTConstant → Text Multiline → WanVideoVAELoader → WanVideoBlockSwap → WanVideoLoraSelect → CLIPVisionLoader → LoadImage → WanVideoModelLoader → OnnxDetectionModelLoader → WanVideoTextEncodeCached → ImageResizeKJv2 → MathExpression|pysssss → WanVideoClipVisionEncode → VHS_LoadVideo
- **P03-动作迁移-Wan2.2Animate循环长视频V2** (99 nodes) — WanVideoBlockSwap → VHS_LoadVideo → WanVideoModelLoader → WanVideoLoraSelectMulti → WanVideoVAELoader → WanVideoTextEncodeCached → CLIPVisionLoader → OnnxDetectionModelLoader → LoadImage → Int → easy mathInt → ImageFromBatch → BatchCount+ → WanVideoAnimateEmbeds
- **P07-动作迁移-Wan2.2AnimateV4** (88 nodes) — CLIPVisionLoader → WanVideoLoraSelectMulti → WanVideoModelLoader → INTConstant → PrimitiveFloat → WanVideoTextEncodeCached → OnnxDetectionModelLoader → WanVideoVAELoader → LoadImage → WanVideoContextOptions → WanVideoBlockSwap → ReservedVRAMSetter → ImageResizeKJv2 → WanVideoClipVisionEncode
  - weights: clip_vision_h.safetensors, umt5-xxl-enc-fp8_e4m3fn.safetensors, wan_2.1_vae.safetensors
- **P22-爱屋Scail2-TTP多参-内循环-面部强化** (54 nodes) — SCAIL2SegmentPlanBuilder → UNETLoader → CLIPLoader → CheckpointLoaderSimple → CLIPVisionLoader → KSamplerSelect → VHS_LoadVideo → VAELoader → LoadImage → LoraLoaderModelOnly → CLIPTextEncode → ImageResizeKJv2 → VHS_VideoInfo → ModelSamplingSD3

## U视频-MINIMAX-H3

- **U00-minimax_h3提示词QWEN3.8群主版** (16 nodes) — LoadImage → ZealmanLLM_ModelLoader → Fast Muter (rgthree) → ZealmanLLM_Generate
- **U00-minimax_h3提示词QWEN3.8群主版V3** (18 nodes) — ZealmanLLM_ModelLoader → CR Prompt Text → LoadImage → Fast Groups Bypasser (rgthree) → H3_Promptor → H3_Vision → PreviewAny
- **U00-selflift群主随便耍耍版** (27 nodes) — KSamplerSelect → ZealmanH3ModelLoader → ZealmanH3PickReferenceMedia → 忽略多组孤海 → MiniMaxChunkFeedForward → MiniMaxH3PromptEnhancerT8 → MiniMaxLowVRAMAttention → AnySwitch → PreviewAny → BasicScheduler → MiniMaxH3ReferenceToVideo → H3SigmaRefiner → ConditioningZeroOut → SenseNovaH3DistilledBridge
  - weights: euler, minimax/minimax_h3_fl2va_bf16.safetensors, qwen3vl_32b_minimax_h3_bf16.safetensors
- **U01-minimax_h3_light2v多图参考生视频加速版** (36 nodes) — VAELoader → KSamplerSelect → UNETLoader → CLIPLoader → RandomNoise → LoadImage → WJILatentPreset → PrimitiveFloat → CR Prompt Text → LoraLoaderModelOnly → ComfyMathExpression → ModelAttentionBackend → MiniMaxH3ReferenceToVideo → MiniMaxLowVRAMAttention
  - weights: euler, minimax/minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors, minimax/minimax_h3_ref2va_int8_convrot.safetensors, minimax_h3_audio_vae_fp32.safetensors
- **U01-minimax_h3_多图参考生视频基础版** (33 nodes) — VAELoader → KSamplerSelect → UNETLoader → RandomNoise → WJILatentPreset → PrimitiveFloat → CR Prompt Text → LoadImage → CLIPLoader → ModelAttentionBackend → ComfyMathExpression → MiniMaxLowVRAMAttention → MiniMaxH3ReferenceToVideo → MiniMaxChunkFeedForward
  - weights: minimax/minimax_h3_ref2va_pruned_int8_convrot.safetensors, minimax_h3_audio_vae_fp32.safetensors, minimax_h3_video_vae_fp16.safetensors, qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
- **U02-minimax_h3_lightX2v首尾帧图生视频加速版V2** (33 nodes) — LoadImage → VAELoader → CLIPLoader → RandomNoise → UNETLoader → KSamplerSelect → WJILatentPreset → PrimitiveFloat → CR Prompt Text → LoraLoaderModelOnly → ComfyMathExpression → ModelAttentionBackend → MiniMaxH3ImageToVideo → MiniMaxLowVRAMAttention
  - weights: euler, minimax/minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors, minimax/minimax_h3_fl2va_pruned_int8_convrot.safetensors, minimax_h3_audio_vae_fp32.safetensors
- **U02-minimax_h3_图生视频基础版** (29 nodes) — LoadImage → WJILatentPreset → VAELoader → KSamplerSelect → CLIPLoader → RandomNoise → UNETLoader → PrimitiveFloat → ModelAttentionBackend → ComfyMathExpression → MiniMaxLowVRAMAttention → MiniMaxH3ImageToVideo → MiniMaxChunkFeedForward → BasicGuider
  - weights: minimax/minimax_h3_fl2va_pruned_int8_convrot.safetensors, minimax_h3_audio_vae_fp32.safetensors, minimax_h3_video_vae_fp16.safetensors, qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
- **U03-minimax_h3_light2v-文生视频加速版** (30 nodes) — VAELoader → KSamplerSelect → CLIPLoader → RandomNoise → WJILatentPreset → PrimitiveFloat → UNETLoader → ComfyMathExpression → LoraLoaderModelOnly → MiniMaxH3ImageToVideo → ModelAttentionBackend → MiniMaxLowVRAMAttention → MiniMaxChunkFeedForward → BasicGuider
  - weights: euler, minimax/minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors, minimax/minimax_h3_fl2va_pruned_int8_convrot.safetensors, minimax_h3_audio_vae_fp32.safetensors
- **U03-minimax_h3_文生视频基础版** (27 nodes) — VAELoader → CLIPLoader → RandomNoise → UNETLoader → KSamplerSelect → WJILatentPreset → PrimitiveFloat → ModelAttentionBackend → ComfyMathExpression → MiniMaxLowVRAMAttention → MiniMaxH3ImageToVideo → MiniMaxChunkFeedForward → BasicGuider → BasicScheduler
  - weights: minimax/minimax_h3_fl2va_pruned_int8_convrot.safetensors, minimax_h3_audio_vae_fp32.safetensors, minimax_h3_video_vae_fp16.safetensors, qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
- **U04-minimax_h3_5图参考生视频30步版** (33 nodes) — VAELoader → KSamplerSelect → UNETLoader → CLIPLoader → RandomNoise → LoadImage → CR Prompt Text → PrimitiveFloat → ResolutionSelector → ModelAttentionBackend → ComfyMathExpression → SolAttnMiniMax → MiniMaxH3ReferenceToVideo → EasyCache
  - weights: er_sde, minimax/minimax_h3_ref2va_bf16.safetensors, minimax_h3_audio_vae_fp32.safetensors, minimax_h3_video_vae_fp16.safetensors
- **U04-minimax_h3_light2v-5图参考生视频加速版** (36 nodes) — VAELoader → KSamplerSelect → UNETLoader → CLIPLoader → RandomNoise → LoadImage → WJILatentPreset → CR Prompt Text → PrimitiveFloat → LoraLoaderModelOnly → ComfyMathExpression → ModelAttentionBackend → MiniMaxH3ReferenceToVideo → MiniMaxLowVRAMAttention
  - weights: euler, minimax/minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors, minimax/minimax_h3_ref2va_int8_convrot.safetensors, minimax_h3_audio_vae_fp32.safetensors
- **U05-MiniMax-H3-一键视频换装** (39 nodes) — KSamplerSelect → PrimitiveInt → PrimitiveStringMultiline → UNETLoader → CLIPLoader → VAELoader → RandomNoise → ZealmanLLM_ModelLoader → LoadImage → PrimitiveFloat → DF_Int_to_Float → BasicScheduler → LoraLoaderModelOnly → ImageResizeKJv2
  - weights: euler, minimax/minimax_h3_ref2va_int8_convrot.safetensors, minimax/minimax_h3_turbo_v4_step600_ema_pruned_comfyui.safetensors, minimax_h3_audio_vae_fp32.safetensors
- **U05-MiniMax-H3-数字人视频带货-多图生视频** (41 nodes) — VAELoader → KSamplerSelect → RandomNoise → LoadImage → PrimitiveFloat → CR Prompt Text → ResolutionSelector → CLIPLoader → UNETLoader → ManualSigmas → BasicScheduler → ComfyMathExpression → ModelAttentionBackend → MiniMaxH3ReferenceToVideo
  - weights: euler, minimax/minimax_h3_ref2va_pruned_fp8_scaled.safetensors, minimax/minimax_h3_turbo_v4_step600_ema_pruned_comfyui.safetensors, minimax_h3_audio_vae_fp32.safetensors
- **U05-minimax_h3-多参考图light2v加速生成-LTX超分** (42 nodes) — VAELoader → CLIPLoader → RandomNoise → LoadImage → KSamplerSelect → UNETLoader → PrimitiveStringMultiline → ResolutionSelector → PrimitiveFloat → LoraLoaderModelOnly → ComfyMathExpression → ModelAttentionBackend → MiniMaxH3ReferenceToVideo → MiniMaxLowVRAMAttention
  - weights: euler, minimax/minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors, minimax/minimax_h3_ref2va_pruned_fp8_scaled.safetensors, minimax_h3_audio_vae_fp32.safetensors
- **U06-minimax_h3_lightX2v多图参考生视频V5** (58 nodes) — VAELoader → CLIPLoader → PrimitiveFloat → LoadImage → easy seed → UNETLoader → VHS_LoadVideo → CR Prompt Text → WJILatentPreset → KSamplerSelect → LoadAudio → ComfyMathExpression → RandomNoise → ModelAttentionBackend
  - weights: euler, minimax/minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors, minimax/minimax_h3_ref2va_pruned_int8_convrot.safetensors, minimax_h3_audio_vae_fp32.safetensors
- **U06-minimax_h3_多图参考生视频V6** (60 nodes) — WJILatentPreset → KSamplerSelect → VHS_LoadVideo → LoadAudio → LoadImage → UNETLoader → VAELoader → CLIPLoader → CR Prompt Text → Fast Groups Muter (rgthree) → PrimitiveFloat → easy seed → ImageResizeKJv2 → TrimAudioDuration
  - weights: euler, minimax/minimax_h3_ref2va_pruned_int8_convrot.safetensors, minimax/minimax_h3_turbo_v4_step600_ema_pruned_comfyui.safetensors, minimax_h3_audio_vae_fp32.safetensors
- **U06-minimax_h3_多图参考生视频V9** (27 nodes) — ZealmanH3PickReferenceMedia → ZealmanH3ModelLoader → KSamplerSelect → RandomNoise → BlockSparseAttention → MiniMaxH3ReferenceToVideo → BasicScheduler → MiniMaxChunkFeedForward → SenseNovaH3DistilledBridge → ConditioningZeroOut → H3SigmaRefiner → BasicGuider → SamplerCustomAdvanced → VAEDecodeAudio
  - weights: er_sde, minimax/Minimax-h3_Singularity_ref2va_v1.3_int8.safetensors, qwen3vl_32b_minimax_h3_int8_convrot.safetensors
- **U08-MiniMax-H3-极速生成10S只要2分半** (36 nodes) — CLIPLoader → VAELoader → ResolutionSelector → PrimitiveFloat → RandomNoise → KSamplerSelect → DiffusionModelLoaderKJ → ManualSigmas → LoadImage → VHS_LoadAudioUpload → PrimitiveStringMultiline → ComfyMathExpression → MiniMaxH3SigmaShift → MMH3LatentUpscaleWithModelParams
  - weights: euler, minimax/minimax_h3_fused_refdelta_r1024_turbo8_mystic07_int8_convrot.safetensors, minimax_h3_audio_vae_fp32.safetensors, minimax_h3_latent_upscaler_3d_fp16.safetensors
- **U09-Minimax-H3二采重绘单模型极速版wuwukasi-V3** (123 nodes) — ResolutionSelector → VAELoader → KSamplerSelect → UNETLoader → CLIPLoader → RandomNoise → PrimitiveFloat → LoadImage → PrimitiveStringMultiline → LoadAudio → Fast Groups Bypasser (rgthree) → INTConstant → UniBlockSwapTE → ComfyMathExpression
  - weights: euler, minimax/minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors, minimax/minimax_h3_ref2va_int8_convrot.safetensors, minimax/minimax_h3_turbo_4step_diffusion_model.safetensors
- **U09-Minimax-H3二采重绘双模型极速版wuwukasi-V4** (132 nodes) — ResolutionSelector → VAELoader → KSamplerSelect → UNETLoader → CLIPLoader → RandomNoise → PrimitiveFloat → LoadImage → PrimitiveStringMultiline → LoadAudio → Fast Groups Bypasser (rgthree) → INTConstant → ExtendIntermediateSigmas → UniBlockSwapTE
  - weights: euler, minimax/minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors, minimax/minimax_h3_ref2va_int8_convrot.safetensors, minimax/minimax_h3_ref2va_pruned_w4a8_mixed.safetensors
- **U0X-H3群主无限版** (17 nodes) — ZealmanH3PickReferenceMedia → KSamplerSelect → ZealmanH3ModelLoader → ZealmanH3Dials → MiniMaxH3ReferenceToVideo → ConditioningZeroOut → BasicScheduler → H3SigmaRefiner → SelfLiftAvatarH3Sampler → VAEDecodeAudio → MiniMaxH3VAEDecodeFast → ZealmanVideoOutput
  - weights: euler, minimax/minimax_h3_fl2va_pruned_int8_convrot.safetensors, qwen3vl_32b_minimax_h3_int8_convrot.safetensors
- **U11-Minimax-H3-图生视频-音频同步V2** (42 nodes) — VAELoader → KSamplerSelect → UNETLoader → CLIPLoader → RandomNoise → VHS_LoadAudioUpload → WJILatentPreset → ZealmanLLM_ModelLoader → DenoPromptText → LoadImage → ModelAttentionBackend → ComfyMathExpression → DenoAudioTranscript → ZealmanH3LoadImageToRefImages
- **U13-MiniMaxH3-黑鹤加速视频流整合** (118 nodes) — LoadImage → ResolutionSelector → VAELoader → KSamplerSelect → UNETLoader → CLIPLoader → PrimitiveFloat → CLIPLoaderGGUF → UnetLoaderGGUF → Fast Groups Bypasser (rgthree) → ImageResizeKJv2 → BasicScheduler → MiniMaxH3MemoryEfficientSageAttentionPatch → ComfyMathExpression
- **U21-H3视频生成双显卡加速-非双显卡勿用** (30 nodes) — CLIPLoader → VAELoader → PrimitiveStringMultiline → PrimitiveFloat → ResolutionSelector → KSamplerSelect → RayInitializer → RayLoraLoader → LoadImage → ComfyMathExpression → RayUNETLoader → MiniMaxH3ReferenceToVideo → RayMiniMaxH3SigmaShift → RayBasicScheduler
  - weights: minimax/minimax_h3_fl2v_turbo_8step_v1.0_768p_comfyui_bf16.safetensors, minimax/minimax_h3_ref2va_pruned_int8_convrot.safetensors, minimax_h3_audio_vae_fp32.safetensors, minimax_h3_video_vae_fp16.safetensors
- **U21-H3视频生成双显卡加速-非双显卡勿用V2** (43 nodes) — CLIPLoader → PrimitiveFloat → LoadImage → CR Prompt Text → LoadAudio → VAELoader → ComfyMathExpression → RayLoraLoader → KSamplerSelect → easy seed → ManualSigmas → Int → WJILatentPreset → TrimAudioDuration
  - weights: euler, minimax/MinimaxH3真实电影质感V0.1.safetensors, minimax/minimax_h3_hybrid_fl2va_ref2va_b25-49-int8.safetensors, minimax/minimax_h3_turbo_v4_step600_ema_pruned_comfyui.safetensors
- **U22-MiniMaxH3-多参考生视频-优化版-YZ金鱼** (122 nodes) — LoadAudio → LoadImage → VHS_LoadVideo → VAELoader → CLIPLoader → UNETLoader → ResolutionSelector → KSamplerSelect → RandomNoise → PrimitiveFloat → easy float → 忽略多组孤海 → CR Prompt Text → MiniMaxH3MemoryEfficientSageAttentionPatch
  - weights: euler, minimax/MysticXXX_MMH3-V1.safetensors, minimax/minimax_h3_hybrid_fl2va_ref2va_b25-49-int8.safetensors, minimax/minimax_h3_turbo_v4_step600_ema_pruned_comfyui.safetensors
- **U22-YZ金鱼-MiniMax-H3-多参考生视频-优化版** (27 nodes) — VAELoader → CLIPLoader → UNETLoader → KSamplerSelect → RandomNoise → ZealmanH3PickReferenceMedia → LoraLoaderModelOnly → MiniMaxH3ReferenceToVideo → ModelAttentionBackend → BasicGuider → BasicScheduler → SplitSigmas → SamplerCustomAdvanced → LTXVSeparateAVLatent
  - weights: euler, minimax/MysticXXX_MMH3-V1.safetensors, minimax/minimax_h3_hybrid_fl2va_ref2va_b25-49-int8.safetensors, minimax/minimax_h3_turbo_v4_step600_ema_pruned_comfyui.safetensors
- **U22-YZ金鱼-MiniMaxH3终极篇-文武双全** (35 nodes) — KSamplerSelect → ZealmanH3PickReferenceMedia → ZealmanH3ModelLoader → BasicScheduler → BlockSparseAttention → MiniMaxH3ReferenceToVideo → MiniMaxH3SigmaShift → ConditioningZeroOut → MiniMaxChunkFeedForward → SelfLiftH3Sampler → VAEDecode → VAEDecodeAudio → VHS_VideoCombine
  - weights: euler, minimax/minimax_h3_hybrid_fl2va_ref2va_b25-49-int8.safetensors, qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
- **U24-文武双修** (37 nodes) — VAELoader → CLIPLoader → UNETLoader → RandomNoise → PrimitiveFloat → ZealmanH3PickReferenceMedia → LoraLoaderBypassModelOnly → MiniMaxH3AudioConditioningT8 → MiniMaxH3MemoryEfficientSageAttentionPatch → ModelAttentionBackend → LoraLoaderModelOnly → MiniMaxH3DualClockSamplerT8 → MiniMaxH3LearnedTwoPassParityPlanT8Advanced → BasicGuider
  - weights: dual_clock_euler, minimax/H3_Combat_V2.safetensors, minimax/MinimaxH3真实电影质感V0.1.safetensors, minimax/Motion_Repair.safetensors
- **U24-文武双修T8版MiniMaxH3双采参考生视频V2** (60 nodes) — VAELoader → CLIPLoader → UNETLoader → RandomNoise → PrimitiveFloat → CR Prompt Text → ResolutionSelector → LoadImage → LoraLoaderBypassModelOnly → ComfyMathExpression → Fast Muter (rgthree) → MiniMaxH3MemoryEfficientSageAttentionPatch → MiniMaxH3AudioConditioningT8 → ModelAttentionBackend
  - weights: dual_clock_euler, minimax/H3_Combat_V2.safetensors, minimax/MinimaxH3真实电影质感V0.1.safetensors, minimax/Motion_Repair.safetensors
- **U24-文武双修T8版MiniMaxH3双采参考生视频V927** (75 nodes) — Float → LoadImage → CR Prompt Text → RandomNoise → PrimitiveFloat → CLIPLoader → VAELoader → MiniMaxH3SemanticBridgeConfigT8 → UNETLoader → ResolutionSelector → easy anythingIndexSwitch → LoraLoaderBypassModelOnly → ComfyMathExpression → ModelAttentionBackend
  - weights: MiniMaxH3_SemanticBridge_v1.safetensors, dual_clock_euler, h3_upscaler_sharpness_2000steps_v0.1_fp32.safetensors, minimax/H3_Combat_V2.safetensors
- **U24-文武双修V927** (49 nodes) — VAELoader → CLIPLoader → UNETLoader → RandomNoise → MiniMaxH3SemanticBridgeConfigT8 → Float → PrimitiveFloat → ZealmanH3PickReferenceMedia → LoraLoaderBypassModelOnly → easy anythingIndexSwitch → MiniMaxH3AudioConditioningT8 → ModelAttentionBackend → MiniMaxH3SemanticBridgeApplyT8 → SolAttnMiniMax
  - weights: MiniMaxH3_SemanticBridge_v1.safetensors, dual_clock_euler, h3_upscaler_sharpness_2000steps_v0.1_fp32.safetensors, minimax/H3_Combat_V2.safetensors
- **U25-Singularity-Vdn文戏版-MiniMaxH3单采极速参考生视频V2-T8** (21 nodes) — VAELoader → CLIPLoader → UNETLoader → RandomNoise → ResolutionSelector → PrimitiveFloat → LoadImage → CR Prompt Text → MiniMaxH3VDNModelComposerT8Advanced → ComfyMathExpression → MiniMaxH3AudioConditioningT8 → MiniMaxH3VDNExecutionPlanT8Advanced → BasicGuider → SamplerCustomAdvanced
  - weights: minimax/Minimax-h3_Singularity_ref2va_v1.3_int8.safetensors, minimax_h3_audio_vae_fp32.safetensors, minimax_h3_video_vae_fp16.safetensors, qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
- **U27-MinimaxH3纹理增强-爱屋** (36 nodes) — CLIPLoader → UNETLoader → RandomNoise → KSamplerSelect → ResolutionSelector → PrimitiveInt → PrimitiveStringMultiline → VAELoader → VHS_LoadVideo → MiniMaxH3SigmaShift → ComfyNumberConvert → CLIPTextEncode → ImageResizeKJv2 → VHS_VideoInfo
  - weights: euler, minimax/minimax_h3_fl2v_lightx2v_turbo_4step_v0.1_comfy.safetensors, minimax/minimax_h3_hybrid_fl2va_ref2va_b30-49-int8.safetensors, minimax/minimax_h3_lms_v1.0_r64.safetensors
- **U28-selflift-Avatar-爱屋自动优化提示词版** (32 nodes) — PrimitiveFloat → ResolutionSelector → CLIPLoader → UNETLoader → KSamplerSelect → LoadImage → VAELoader → PrimitiveStringMultiline → ZealmanLLM_ModelLoader → ComfyMathExpression → ModelAttentionBackend → ZealmanLLM_H3Prompt → LoraLoaderModelOnly → PreviewAny
  - weights: euler, minimax/H3_speed_slider_1.1.safetensors, minimax/dmad_minimax_h3_4step_full_critic_comfy.safetensors, minimax/minimax_h3_hybrid_fl2va_ref2va_b25-49-int8.safetensors
- **U28-双采数字人-self-lift工作流-爱屋** (37 nodes) — SolidMask → KSamplerSelect → UNETLoader → CLIPLoader → VAELoader → ResolutionSelector → LoadAudio → LoadImage → LoraLoaderModelOnly → TrimAudioDuration → MiniMaxH3PromptEnhancerT8 → ModelAttentionBackend → SoundFlow_GetLength → LTXVAudioVAEEncode
  - weights: euler, minimax/minimax_h3_fl2v_lightx2v_turbo_4step_v0.1_comfy.safetensors, minimax/minimax_h3_fl2va_bf16.safetensors, minimax_h3_audio_vae_fp32.safetensors
- **U28-黑科技加速双采-self-lift工作流-爱屋** (30 nodes) — KSamplerSelect → UNETLoader → CLIPLoader → VAELoader → PrimitiveFloat → LoadImage → PrimitiveStringMultiline → ResolutionSelector → ModelAttentionBackend → ComfyMathExpression → LoraLoaderModelOnly → MiniMaxH3ReferenceToVideo → MiniMaxLowVRAMAttention → ConditioningZeroOut
  - weights: euler, minimax/minimax_h3_fl2v_lightx2v_turbo_4step_v0.1_comfy.safetensors, minimax/minimax_h3_fl2va_bf16.safetensors, minimax_h3_audio_vae_fp32.safetensors
- **U30-Minimax-H3-Singularity超双采放大-AIGC特异点** (85 nodes) — KSamplerSelect → RandomNoise → DisableNoise → easy float → ZealmanH3PickReferenceMedia → ZealmanH3ModelLoader → MiniMaxH3ReferenceToVideo → BlockSparseAttention → BasicScheduler → SenseNovaH3DistilledBridge → MiniMaxLowVRAMAttention → ExtendIntermediateSigmas → BasicGuider → MiniMaxChunkFeedForward
  - weights: euler, minimax/Minimax-h3_Singularity_ref2va_v1.3_int8.safetensors, minimax_h3_latent_upscaler_3d_bf16.safetensors, qwen3vl_32b_minimax_h3_int8_convrot.safetensors
- **U30-Minimax-H3-Singularity超双采放大-AIGC特异点V2** (87 nodes) — KSamplerSelect → RandomNoise → CLIPLoader → VAELoader → UNETLoader → DisableNoise → easy float → ZealmanH3PickReferenceMedia → ModelAttentionBackend → BasicScheduler → LoraLoaderModelOnly → BlockSparseAttention → ExtendIntermediateSigmas → MiniMaxLowVRAMAttention
  - weights: euler, minimax/Minimax-h3_Singularity_ref2va_v2_int8.safetensors, minimax/minimax_h3_lms_v1.0_r64.safetensors, minimax_h3_audio_vae_fp32.safetensors
- **U35-H3官流-单采文戏-神棍** (37 nodes) — ResolutionSelector → LoadImage → LoadAudio → VHS_LoadVideo → PrimitiveFloat → PrimitiveStringMultiline → CLIPLoader → VAELoader → KSamplerSelect → RandomNoise → UNETLoader → ComfyMathExpression → LoraLoaderModelOnly → MiniMaxH3ReferenceToVideo
  - weights: er_sde, h3-realism-people-t2v-i2v-r2v.safetensors, minimax/Cobijada_H3_Hybrid_Uncensored_pruned_hybrid_int8_convrot_pruned.safetensors, minimax/minimax_h3_DMAD_4step_full_lora_avg_rank_39_bf16.safetensors
- **U35-H3官流-最强武戏-神棍** (38 nodes) — ResolutionSelector → KSamplerSelect → ManualSigmas → LoadImage → LoadAudio → VHS_LoadVideo → PrimitiveFloat → PrimitiveStringMultiline → CLIPLoader → VAELoader → UNETLoader → RandomNoise → CR Prompt Text → ComfyMathExpression
  - weights: er_sde, minimax/Cobijada_H3_Hybrid_Uncensored_pruned_hybrid_int8_convrot_pruned.safetensors, minimax/H3_Combat_V2.safetensors, minimax/Motion_Repair.safetensors
- **U35-H3官流-终极版-神棍** (36 nodes) — UNETLoader → CLIPLoader → VAELoader → PrimitiveFloat → ResolutionSelector → RandomNoise → LoadImage → PrimitiveStringMultiline → KSamplerSelect → ManualSigmas → LoadAudio → VHS_LoadVideo → LoraLoaderModelOnly → ComfyMathExpression
  - weights: er_sde, h3-realism-people-t2v-i2v-r2v.safetensors, minimax/Cobijada_H3_Hybrid_Uncensored_pruned_hybrid_int8_convrot_pruned.safetensors, minimax/minimax_h3_ref2v_turbo_8step_v1.0_768p_comfyui_bf16.safetensors
- **U39-H3无损融合单采** (23 nodes) — KSamplerSelect → UNETLoader → RandomNoise → ManualSigmas → CLIPLoader → VAELoader → ZealmanH3PickReferenceMedia → LoraLoaderModelOnly → MiniMaxH3ReferenceToVideo → ModelAttentionBackend → BasicGuider → BlockSparseAttention → SamplerCustomAdvanced → VAEDecode
  - weights: er_sde, minimax/Cobijada_H3_Hybrid_Uncensored_pruned_hybrid_int8_convrot_pruned.safetensors, minimax/minimax_h3_ref2v_turbo_8step_v1.0_768p_comfyui_bf16.safetensors, minimax_h3_audio_vae_fp32.safetensors
- **U39-吃猪侠233-2采** (101 nodes) — LoadAudio → VHS_LoadVideo → VAELoader → CLIPLoader → LoadImage → UNETLoader → ResolutionSelector → KSamplerSelect → RandomNoise → PrimitiveFloat → easy float → 忽略多组孤海 → CR Prompt Text → ModelAttentionBackend
  - weights: er_sde, euler, minimax/minimax_h3_hybrid_fl2va_ref2va_b25-49-int8.safetensors, minimax/minimax_h3_ref2v_turbo_8step_v1.0_768p_comfyui_bf16.safetensors
- **U39-吃猪侠233-H3无损融合单采** (75 nodes) — LoadAudio → LoadImage → KSamplerSelect → RandomNoise → 忽略多组孤海 → VHS_LoadVideo → VAELoader → ManualSigmas → UNETLoader → CLIPLoader → PrimitiveFloat → ResolutionSelector → PrimitiveStringMultiline → MiniMaxH3ReferenceToVideo
  - weights: er_sde, minimax/Cobijada_H3_Hybrid_Uncensored_pruned_hybrid_int8_convrot_pruned.safetensors, minimax/minimax_h3_ref2v_turbo_8step_v1.0_768p_comfyui_bf16.safetensors, minimax_h3_audio_vae_fp32.safetensors
- **U39-吃猪侠233单采V2-33步雷霆祭祀版** (75 nodes) — ZealmanH3PickReferenceMedia → ZealmanH3ModelLoader → KSamplerSelect → RandomNoise → MiniMaxH3ReferenceToVideo → BlockSparseAttention → BasicScheduler → BasicGuider → MiniMaxH3SigmaShift → SamplerCustomAdvanced → MiniMaxChunkFeedForward → VAEDecodeAudio → VAEDecode → VHS_VideoCombine
  - weights: er_sde, minimax/Cobijada_H3_Hybrid_Uncensored_pruned_hybrid_int8_convrot_pruned.safetensors, qwen3vl_32b_minimax_h3_int8_convrot.safetensors
- **U45-RemakeH3视频编辑** (17 nodes) — KSamplerSelect → ManualSigmas → ZealmanH3PickReferenceMedia → ZealmanH3ModelLoader → RemakeKeyframeUntil → RemakeConditioning → RemakeNoise → BasicGuider → SamplerCustomAdvanced → VAEDecode → VAEDecodeAudio → ZealmanVideoOutput
  - weights: euler, minimax/minimax_h3_fl2va_pruned_int8_convrot.safetensors, qwen3vl_32b_minimax_h3_int8_convrot.safetensors
- **U46-RemakeH3视频替换** (17 nodes) — KSamplerSelect → ManualSigmas → ZealmanH3PickReferenceMedia → ZealmanH3ModelLoader → RemakeKeyframeUntil → RemakeConditioning → RemakeNoise → BasicGuider → SamplerCustomAdvanced → VAEDecode → VAEDecodeAudio → ZealmanVideoOutput
  - weights: euler, minimax/minimax_h3_fl2va_pruned_int8_convrot.safetensors, qwen3vl_32b_minimax_h3_int8_convrot.safetensors
- **U47-TaoMateHD数字人** (27 nodes) — UNETLoader → CLIPLoader → VAELoader → LoadImage → LoadAudio → SolidMask → ResolutionSelector → PrimitiveFloat → LoraLoaderModelOnly → TrimAudioDuration → ComfyMathExpression → ModelAttentionBackend → LTXVAudioVAEEncode → MiniMaxH3ReferenceToVideo
  - weights: minimax/TaoMate-HD-preview-comfy.safetensors, minimax/minimax_h3_hybrid_fl2va_ref2va_b25-49-int8.safetensors, minimax_h3_audio_vae_fp32.safetensors, minimax_h3_video_vae_fp16.safetensors
- **U48-P-H3图像编辑Singularity版** (25 nodes) — UNETLoader → KSamplerSelect → RandomNoise → CLIPLoader → VAELoader → ManualSigmas → ZealmanH3PickReferenceMedia → LoraLoaderBypassModelOnly → BatchImagesNode → StringFormat → MiniMaxH3SigmaShift → TextGenerate → MiniMaxH3MemoryEfficientSageAttentionPatch → ComfySwitchNode
  - weights: euler, minimax/Minimax-h3_Singularity_ref2va_v1.3_int8.safetensors, minimax/pika_h3_flex_fl2va_v1_bf16.safetensors, p-h3-image_prompt_upsampler_int8_convrot.safetensors

## Y通用制作

- **Y01-图像修改千问2511** (27 nodes) — INTConstant → LoadImage → CLIPLoader → VAELoader → UNETLoader → LayerUtility: ImageScaleByAspectRatio V2 → LoraLoaderModelOnly → TextEncodeQwenImageEditPlus → VAEEncode → CFGNorm → ReferenceLatent → KSampler → VAEDecode → PlaySound|pysssss
- **Y02-图像修改克莱因** (24 nodes) — KSamplerSelect → RandomNoise → VAELoader → LoadImage → CLIPLoader → UNETLoader → ImageScaleToTotalPixels → CLIPTextEncode → LoraLoaderModelOnly → VAEEncode → GetImageSize → ConditioningZeroOut → ReferenceLatent → EmptyFlux2LatentImage
- **Y03-图像修改FireRed** (25 nodes) — PrimitiveInt → PrimitiveFloat → CLIPLoader → VAELoader → PrimitiveBoolean → UNETLoader → LoadImage → Switch any [Crystools] → LoraLoaderModelOnly → FluxKontextImageScale → TextEncodeQwenImageEditPlus → VAEEncode → ModelSamplingAuraFlow → CFGNorm
- **Y04-图像生成Zimage** (19 nodes) — CLIPLoader → UNETLoader → VAELoader → INTConstant → CLIPTextEncode → EmptySD3LatentImage → ConditioningZeroOut → KSampler → VAEDecode → ImageScaleBy → VAEEncode → SaveImage
- **Y05-图像生成Qwen2512** (18 nodes) — CLIPLoader → VAELoader → UNETLoader → INTConstant → CLIPTextEncode → LoraLoaderModelOnly → CR SDXL Aspect Ratio → KSampler → VAEDecode → SaveImage
- **Y06-图像改为下一个场景图** (19 nodes) — Int → CLIPLoader → VAELoader → UNETLoader → LoadImage → LoraLoaderModelOnly → LayerUtility: ImageScaleByAspectRatio V2 → TextEncodeQwenImageEditPlus → VAEEncode → KSampler → VAEDecode → SaveImage
- **Y07-Klein-文生图** (19 nodes) — PrimitiveStringMultiline → KSamplerSelect → RandomNoise → CLIPLoader → VAELoader → UNETLoader → INTConstant → CLIPTextEncode → EmptyFlux2LatentImage → Flux2Scheduler → CFGGuider → SamplerCustomAdvanced → VAEDecode → SaveImage
- **Y08-四宫格-LTX-2.3图生视频优化版** (70 nodes) — LatentUpscaleModelLoader → VAELoaderKJ → DualCLIPLoader → RandomNoise → KSamplerSelect → ManualSigmas → TTResolutionSelector → VAELoader → UNETLoader → INTConstant → PrimitiveFloat → LoadImage → CR Prompt Text → EmptyLTXVLatentVideo

## Z工具设置

- **Z01-工具-ZealmanAPI示例** (8 nodes) — DeepSeekV4Node → AutodlApiNode → DoubaoNode → DoubaoSeedream5Node → DoubaoSeedTranslationNode
- **Z02-工具-通用替换模组** (31 nodes) — llama_cpp_parameters → llama_cpp_model_loader → Qwen3_VQA → LoadImage → VHS_LoadVideo → llama_cpp_instruct_adv
- **Z03-工具-批量描述生成器** (24 nodes) — KepStringLiteral → llama_cpp_parameters → llama_cpp_model_loader → Text Concatenate → llama_cpp_instruct_adv → segment_text
- **Z04-设置-ComfyUI批量加载** (9 nodes) — Load Image Batch → VHS_LoadVideo
- **Z05-设置-ComfyUI视频帧数设置** (9 nodes) — VHS_VideoCombine → INTConstant → VHS_LoadVideo → MathExpression|pysssss
- **Z06-设置-API重复调用清缓存** (19 nodes) — VAEDecode → ImageFromBatch → RIFE VFI → SaveImage → VHS_VideoCombine
- **Z07-设置-最后一帧输出图像** (8 nodes) — VAEDecode → VHS_VideoCombine → Pick From Batch (mtb) → ImageScaleBy → SaveImage
- **Z08-设置-视频补帧** (6 nodes) — RIFE VFI → PrimitiveFloat → VHS_VideoCombine
- **Z09-视频补帧-防丢帧-防偏色** (18 nodes) — DownloadAndLoadGIMMVFIModel → easy int → VHS_LoadVideoFFmpeg → CM_IntToFloat → VHS_VideoInfo → CM_FloatBinaryOperation → easy mathInt → ImageFromBatch → MathExpression|pysssss → RepeatImageBatch → ImageBatch → GIMMVFI_interpolate → VHS_VideoCombine
- **Z10-视频补帧-长视频** (8 nodes) — DownloadAndLoadGIMMVFIModel → easy float → LoadVideo → GIMMVFI_stream
- **Z11-XY图表测试工作流** (41 nodes) — INTConstant → VAELoader → UNETLoader → CR Text → easy loraStack → CLIPLoader → LazySwitch2way → easy forLoopStart → SimpleMath+ → easy loraStackApply → EmptyLatentImage → easy promptLine → Lora Loader → CLIPTextEncode
