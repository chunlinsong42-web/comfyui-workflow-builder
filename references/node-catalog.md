> 说明：本目录由**参考实例**的 /object_info 生成，节点名与参数随 ComfyUI/自定义节点版本变化；使用前以你自己的 comfy.py catalog 结果为准。

# 节点目录（自动生成，来自当前实例的 /object_info）

共 6619 个节点类型可用；下方为「150 个工作流实际用到的节点 + 常用核心节点」的签名摘要。
格式：`节点名` [分类] — in: 输入(默认值用 «» 标出) | out: 输出名/类型。
需要完整清单时运行 `python scripts/comfy.py nodes <关键词>`；需要全部 6000+ 节点时读取 .cache/object_info.json。

## loaders
- `OTUNetLoaderW8A8` [loaders] — in: unet_name=«Chroma1/Chroma1-HD-fp8_scaled_rev2.safetensors», weight_dtype=«default», model_type=«flux2», on_the_fly_quantization:BOOLEAN, enable_convrot:BOOLEAN, lora_mode=«None» | out: MODEL

## AIFSH_XTTS
- `SoundFlow_GetLength` [AIFSH_XTTS] — in: audio:AUDIO | out: FLOAT

## BSS
- `AnimaBoosterCheckpointLoader` [BSS/AnimaBooster] — in: ckpt_name=«10Eros_v1-fp8mixed_learned.safetensors», sage_attention=«auto», torch_compile:BOOLEAN | out: model, clip, vae
- `AnimaTeaCache` [BSS/AnimaBooster] — in: model:MODEL, threshold:FLOAT, teacache_version=«v1 (Legacy Fast)», adaptive_mode:BOOLEAN, early_steps_factor:FLOAT, late_steps_factor:FLOAT | out: model

## CogVideoWrapper
- `CogVideoEnhanceAVideo` [CogVideoWrapper] — in: weight:FLOAT, start_percent:FLOAT, end_percent:FLOAT | out: feta_args

## ComfyUI-Frame-Interpolation
- `RIFE VFI` [ComfyUI-Frame-Interpolation/VFI] — in: ckpt_name=«rife49.pth», frames:IMAGE, clear_cache_after_n_frames:INT, multiplier:INT, fast_mode:BOOLEAN, ensemble:BOOLEAN, scale_factor=«1.0», dtype=«float32», torch_compile:BOOLEAN, batch_size:INT | out: IMAGE

## Comfyui_Qwen3-VL-Instruct
- `Qwen3_VQA` [Comfyui_Qwen3-VL-Instruct] — in: text:STRING, model=«Qwen3-VL-4B-Instruct-FP8», quantization=«none», keep_model_loaded:BOOLEAN, temperature:FLOAT, max_new_tokens:INT, min_pixels:INT, max_pixels:INT, seed:INT, attention=«eager» | out: STRING

## ControlNet Preprocessors
- `AIO_Preprocessor` [ControlNet Preprocessors] — in: image:IMAGE | out: IMAGE
- `DepthAnythingV2Preprocessor` [ControlNet Preprocessors/Normal and Depth Estimators] — in: image:IMAGE | out: IMAGE

## Deno
- `DenoAudioAnalysisFinalize` [Deno/Audio] — in: analysis:STRING, clip:CLIP, model_after_run=«Unload after run» | out: audio_context
- `DenoAudioTranscript` [Deno/Audio] — in: audio:AUDIO, model=«large-v3-turbo», language=«auto», model_after_run=«Unload after run» | out: audio_context, transcript, audio
- `DenoPromptText` [Deno/Prompt] — in: text:STRING | out: text

## Derfuu_Nodes
- `DF_Int_to_Float` [Derfuu_Nodes/Functions/Converters] — in: Value:INT | out: FLOAT

## EasyUse
- `easy anythingIndexSwitch` [EasyUse/Logic/Index Switch] — in: index:INT | out: value
- `easy batchAnything` [EasyUse/Logic] — in: any_1:*, any_2:* | out: batch
- `easy cleanGpuUsed` [EasyUse/Logic] — in: anything:* | out: output
- `easy clearCacheAll` [EasyUse/Logic] — in: anything:* | out: output
- `easy compare` [EasyUse/Logic/Math] — in: - | out: boolean
- `easy float` [EasyUse/Logic/Type] — in: value:FLOAT | out: float
- `easy forLoopEnd` [EasyUse/Logic/For Loop] — in: flow:FLOW_CONTROL | out: value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13, value14, value15, value16, value17, value18, value19
- `easy forLoopStart` [EasyUse/Logic/For Loop] — in: total:INT | out: flow, index, value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13, value14, value15, value16, value17, value18, value19
- `easy hiresFix` [EasyUse/Fix] — in: model_name=«1x-ITF-SkinDiffDetail-Lite-v1.pth», rescale_after_model=«True», rescale_method=«nearest-exact», rescale=«by percentage», percent:INT, width:INT, height:INT, longer_side:INT, crop=«disabled», image_output=«… | out: pipe, image, latent
- `easy ifElse` [EasyUse/Logic] — in: boolean:BOOLEAN, on_true:*, on_false:* | out: *
- `easy imageBatchToImageList` [EasyUse/Image] — in: image:IMAGE | out: IMAGE
- `easy imageColorMatch` [EasyUse/Image] — in: image_ref:IMAGE, image_target:IMAGE, method=«wavelet», image_output=«Preview», save_prefix:STRING | out: image
- `easy imageListToImageBatch` [EasyUse/Image] — in: images:IMAGE | out: IMAGE
- `easy imageSize` [EasyUse/Image] — in: image:IMAGE | out: width_int, height_int
- `easy imageSizeBySide` [EasyUse/Image] — in: image:IMAGE, side=«Longest» | out: resolution
- `easy int` [EasyUse/Logic/Type] — in: value:INT | out: int
- `easy loraStack` [EasyUse/Loaders] — in: toggle:BOOLEAN, mode=«simple», num_loras:INT | out: lora_stack
- `easy loraStackApply` [EasyUse/Adapter] — in: lora_stack:LORA_STACK, model:MODEL | out: model, clip
- `easy mathInt` [EasyUse/Logic/Math] — in: a:INT, b:INT, operation=«add» | out: INT
- `easy positive` [EasyUse/Prompt] — in: positive:STRING | out: positive
- `easy promptLine` [EasyUse/Prompt] — in: prompt:STRING, start_index:INT, max_rows:INT, remove_empty_lines:BOOLEAN | out: STRING, COMBO
- `easy promptList` [EasyUse/Prompt] — in: prompt_1:STRING, prompt_2:STRING, prompt_3:STRING, prompt_4:STRING, prompt_5:STRING | out: prompt_list, prompt_strings
- `easy promptReplace` [EasyUse/Prompt] — in: prompt:STRING | out: prompt
- `easy seed` [EasyUse/Seed] — in: seed:INT | out: seed
- `easy showAnything` [EasyUse/Logic] — in: - | out: output

## FishAudioS2
- `FishS2MultiSpeakerTTS` [FishAudioS2] — in: model_path=«s2-pro», text:STRING, language=«auto», device=«auto», precision=«auto», attention=«auto», max_new_tokens:INT, chunk_length:INT, temperature:FLOAT, top_p:FLOAT, repetition_penalty:FLOAT, seed:INT, keep_mode… | out: audio
- `FishS2TTS` [FishAudioS2] — in: model_path=«s2-pro», text:STRING, language=«auto», device=«auto», precision=«auto», attention=«auto», max_new_tokens:INT, chunk_length:INT, temperature:FLOAT, top_p:FLOAT, repetition_penalty:FLOAT, seed:INT, keep_mode… | out: audio
- `FishS2VoiceCloneTTS` [FishAudioS2] — in: model_path=«s2-pro», text:STRING, reference_audio:AUDIO, language=«auto», device=«auto», precision=«auto», attention=«auto», max_new_tokens:INT, chunk_length:INT, temperature:FLOAT, top_p:FLOAT, repetition_penalty:FLO… | out: audio

## FlashVSR
- `FlashVSRInitPipe` [FlashVSR] — in: model=«FlashVSR-v1.1», mode=«tiny», alt_vae=«none», force_offload:BOOLEAN, precision=«bf16», device=«auto», attention_mode=«sparse_sage_attention» | out: pipe
- `FlashVSRNodeAdv` [FlashVSR] — in: pipe:PIPE, frames:IMAGE, scale:INT, color_fix:BOOLEAN, tiled_vae:BOOLEAN, tiled_dit:BOOLEAN, tile_size:INT, tile_overlap:INT, unload_dit:BOOLEAN, sparse_ratio:FLOAT, kv_ratio:FLOAT, local_range:INT, seed:INT | out: image

## Florence2
- `DownloadAndLoadFlorence2Model` [Florence2] — in: model=«microsoft/Florence-2-base», precision=«fp16» | out: florence2_model
- `Florence2Run` [Florence2] — in: image:IMAGE, florence2_model:FL2MODEL, text_input:STRING, task=«region_caption», fill_mask:BOOLEAN | out: image, mask, caption, data

## GIMM-VFI
- `DownloadAndLoadGIMMVFIModel` [GIMM-VFI] — in: model=«gimmvfi_r_arb_lpips_fp32.safetensors» | out: gimmvfi_model

## ImageSaver
- `Image Saver Simple` [ImageSaver] — in: images:IMAGE, filename:STRING, path:STRING, extension=«png», lossless_webp:BOOLEAN, quality_jpeg_or_webp:INT, optimize_png:BOOLEAN, embed_workflow:BOOLEAN, save_workflow_as_json:BOOLEAN | out: hashes, a1111_params
- `Seed Generator (Image Saver)` [ImageSaver/utils] — in: seed:INT, increment:INT | out: INT

## ImageSaverTools
- `Cfg Literal` [ImageSaverTools/utils] — in: float:FLOAT | out: FLOAT

## ImpactPack
- `FaceDetailer` [ImpactPack/Simple] — in: image:IMAGE, model:MODEL, clip:CLIP, vae:VAE, guide_size:FLOAT, guide_size_for:BOOLEAN, max_size:FLOAT, seed:INT, steps:INT, cfg:FLOAT, sampler_name=«euler», scheduler=«simple», positive:CONDITIONING, negative:CONDITI… | out: image, cropped_refined, cropped_enhanced_alpha, mask, detailer_pipe, cnet_images
- `FaceDetailerPipe` [ImpactPack/Simple] — in: image:IMAGE, detailer_pipe:DETAILER_PIPE, guide_size:FLOAT, guide_size_for:BOOLEAN, max_size:FLOAT, seed:INT, steps:INT, cfg:FLOAT, sampler_name=«euler», scheduler=«simple», denoise:FLOAT, feather:INT, noise_mask:BOOL… | out: image, cropped_refined, cropped_enhanced_alpha, mask, detailer_pipe, cnet_images
- `ImageListToImageBatch` [ImpactPack/Operation] — in: images:IMAGE | out: IMAGE
- `ImpactExecutionOrderController` [ImpactPack/Util] — in: signal:*, value:* | out: signal, value
- `ImpactImageBatchToImageList` [ImpactPack/Util] — in: image:IMAGE | out: IMAGE
- `ImpactInt` [ImpactPack/Logic] — in: value:INT | out: INT
- `ImpactSwitch` [ImpactPack/Util] — in: select:INT, sel_mode:BOOLEAN | out: selected_value, selected_label, selected_index
- `ImpactWildcardEncode` [ImpactPack/Prompt] — in: model:MODEL, clip:CLIP, wildcard_text:STRING, populated_text:STRING, mode=«populate», Select to add LoRA=«Select the LoRA to add to the text», Select to add Wildcard=«Select the Wildcard to add to the text», seed:INT | out: model, clip, conditioning, populated_text
- `SAMLoader` [ImpactPack] — in: model_name=«SeC-4B-bf16.safetensors», device_mode=«AUTO» | out: SAM_MODEL
- `UltralyticsDetectorProvider` [ImpactPack] — in: model_name=«bbox/face_yolov8m.pt» | out: BBOX_DETECTOR, SEGM_DETECTOR

## JPS Nodes
- `Sampler Scheduler Settings (JPS)` [JPS Nodes/Settings] — in: sampler_name=«euler», scheduler=«simple» | out: sampler_name, scheduler

## KJNodes
- `AddLabel` [KJNodes/text] — in: image:IMAGE, text_x:INT, text_y:INT, height:INT, font_size:INT, font_color:STRING, label_color:STRING, font=«FreeMono.ttf», text:STRING, direction=«up» | out: IMAGE
- `ColorMatch` [KJNodes/image] — in: image_ref:IMAGE, image_target:IMAGE, method=«mkl» | out: image
- `DiffusionModelLoaderKJ` [KJNodes/model_loaders] — in: model_name=«Chroma1/Chroma1-HD-fp8_scaled_rev2.safetensors», weight_dtype=«default», compute_dtype=«default», patch_cublaslinear:BOOLEAN, sage_attention=«False», enable_fp16_accumulation:BOOLEAN | out: MODEL
- `DrawMaskOnImage` [KJNodes/masking] — in: image:IMAGE, mask:MASK, color:STRING | out: images
- `FloatConstant` [KJNodes/constants] — in: value:FLOAT | out: value
- `GetImageRangeFromBatch` [KJNodes/image] — in: start_index:INT, num_frames:INT | out: IMAGE, MASK
- `GetImageSizeAndCount` [KJNodes/image] — in: image:IMAGE | out: image, width, height, count
- `INTConstant` [KJNodes/constants] — in: value:INT | out: value
- `ImageAndMaskPreview` [KJNodes/masking] — in: mask_opacity:FLOAT, mask_color:STRING, pass_through:BOOLEAN | out: composite
- `ImageConcatMulti` [KJNodes/image] — in: inputcount:INT, image_1:COMFY_MATCHTYPE_V3, direction=«right», match_image_size:BOOLEAN | out: output
- `ImageResizeKJv2` [KJNodes/image] — in: image:IMAGE, width:INT, height:INT, upscale_method=«nearest-exact», keep_proportion=«False», pad_color:STRING, crop_position=«center», divisible_by:INT | out: IMAGE, width, height, mask
- `ImageUpscaleWithModelBatched` [KJNodes/image] — in: upscale_model:UPSCALE_MODEL, images:IMAGE, per_batch:INT | out: IMAGE
- `JoinStringMulti` [KJNodes/text] — in: inputcount:INT, string_1:STRING, delimiter:STRING, return_list:BOOLEAN | out: string
- `JoinStrings` [KJNodes/text] — in: delimiter:STRING | out: STRING
- `LTX2AttentionTunerPatch` [KJNodes/ltxv] — in: model:MODEL, blocks:STRING, video_scale:FLOAT, audio_scale:FLOAT, audio_to_video_scale:FLOAT, video_to_audio_scale:FLOAT, triton_kernels:BOOLEAN | out: model
- `LTX2AudioLatentNormalizingSampling` [KJNodes/ltxv] — in: model:MODEL, audio_normalization_factors:STRING | out: MODEL
- `LTX2MemoryEfficientSageAttentionPatch` [KJNodes/ltxv] — in: model:MODEL, triton_kernels:BOOLEAN | out: model
- `LTX2SamplingPreviewOverride` [KJNodes/ltxv] — in: model:MODEL, preview_rate:FLOAT,INT | out: MODEL
- `LTX2_NAG` [KJNodes/ltxv] — in: model:MODEL, nag_scale:FLOAT, nag_alpha:FLOAT, nag_tau:FLOAT | out: model
- `LTXVAddGuideMulti` [KJNodes/ltxv] — in: positive:CONDITIONING, negative:CONDITIONING, vae:VAE, latent:LATENT, num_guides:COMFY_DYNAMICCOMBO_V3 | out: positive, negative, latent
- `LTXVChunkFeedForward` [KJNodes/ltxv] — in: model:MODEL, chunks:INT, dim_threshold:INT | out: model
- `LTXVImgToVideoInplaceKJ` [KJNodes/ltxv] — in: vae:VAE, latent:LATENT, num_images:COMFY_DYNAMICCOMBO_V3 | out: latent
- `LazySwitchKJ` [KJNodes/misc] — in: switch:BOOLEAN, on_false:*, on_true:* | out: *
- `MiniMaxChunkFeedForward` [KJNodes/experimental] — in: model:MODEL, chunks:INT, seq_threshold:INT | out: model
- `MiniMaxH3MemoryEfficientSageAttentionPatch` [KJNodes/minimax] — in: model:MODEL | out: model
- `MiniMaxLowVRAMAttention` [KJNodes/experimental] — in: model:MODEL, head_chunks:INT | out: model
- `ModelPatchTorchSettings` [KJNodes/experimental] — in: model:MODEL, enable_fp16_accumulation:BOOLEAN | out: MODEL
- `ModelPreviewOverrideKJ` [KJNodes/sampling] — in: model:MODEL, max_resolution:INT, jpeg_quality:INT, suppress_default_preview:BOOLEAN, preview_frames:INT, preview_fps:INT | out: MODEL
- `PathchSageAttentionKJ` [KJNodes/experimental] — in: model:MODEL, sage_attention=«False» | out: MODEL
- `SaveImageKJ` [KJNodes/image] — in: images:IMAGE, filename_prefix:STRING, output_folder:STRING | out: filename
- `SeparateMasks` [KJNodes/masking] — in: mask:MASK, size_threshold_width:INT, size_threshold_height:INT, mode=«convex_polygons», max_poly_points:INT | out: mask
- `SimpleCalculatorKJ` [KJNodes/misc] — in: expression:STRING, variables:COMFY_AUTOGROW_V3 | out: FLOAT, INT, BOOLEAN
- `VAELoaderKJ` [KJNodes/vae] — in: vae_name=«Krea2-HD-vae.safetensors», device=«main_device», weight_dtype=«bf16» | out: VAE
- `VRAM_Debug` [KJNodes/memory] — in: empty_cache:BOOLEAN, gc_collect:BOOLEAN, unload_all_models:BOOLEAN | out: any_output, image_pass, model_pass, freemem_before, freemem_after
- `VisualizeSigmasKJ` [KJNodes/misc] — in: sigmas:SIGMAS, start_step:INT, end_step:INT | out: sigmas_out, image
- `WanVideoNAG` [KJNodes/wan] — in: model:MODEL, conditioning:CONDITIONING, nag_scale:FLOAT, nag_alpha:FLOAT, nag_tau:FLOAT | out: model

## Krea2
- `Krea2ControlApply` [Krea2/control] — in: model:MODEL, control_latent:LATENT | out: MODEL
- `Krea2ControlImageEncode` [Krea2/control] — in: control_image:IMAGE, vae:VAE, resize=«match_latent_size», upscale_method=«lanczos», crop=«center», channel_mode=«rgb», normalize=«none», invert:BOOLEAN, batch_mode=«independent_images» | out: control_latent, encoded_control_image
- `Krea2ControlLoRALoader` [Krea2/control] — in: model:MODEL, lora_name=«Aura_Phantasy_illu.safetensors», strength:FLOAT | out: MODEL

## LCS
- `LCSColorAnchor` [LCS/intervention] — in: model:MODEL, lcs_data:LCS_DATA, mode=«auto», intensity:FLOAT | out: model
- `LCSLoadData` [LCS/calibration] — in: vae:VAE | out: lcs_data
- `LCSSharpnessCalibrate` [LCS/calibration] — in: vae:VAE | out: sharpness_data
- `LCSSharpnessIntervene` [LCS/intervention] — in: model:MODEL, sharpness_data:SHARPNESS_DATA, strength:FLOAT, start_step:INT, end_step:INT | out: model

## Lightricks
- `LTXAddVideoICLoRAGuide` [Lightricks/IC-LoRA] — in: positive:CONDITIONING, negative:CONDITIONING, vae:VAE, latent:LATENT, image:IMAGE, frame_idx:INT, strength:FLOAT, latent_downscale_factor:FLOAT, crop=«disabled», use_tiled_encode:BOOLEAN, tile_size:INT, tile_overlap:INT | out: positive, negative, latent

## Literals
- `Float` [Literals] — in: Number:STRING | out: FLOAT
- `Int` [Literals] — in: Number:STRING | out: INT
- `KepStringLiteral` [Literals] — in: String:STRING | out: STRING
- `String` [Literals] — in: String:STRING | out: STRING

## MMAudio
- `MMAudioFeatureUtilsLoader` [MMAudio] — in: vae_model=«apple_DFN5B-CLIP-ViT-H-14-384_fp16.safetensors», synchformer_model=«apple_DFN5B-CLIP-ViT-H-14-384_fp16.safetensors», clip_model=«apple_DFN5B-CLIP-ViT-H-14-384_fp16.safetensors» | out: mmaudio_featureutils
- `MMAudioModelLoader` [MMAudio] — in: mmaudio_model=«apple_DFN5B-CLIP-ViT-H-14-384_fp16.safetensors», base_precision=«fp16» | out: mmaudio_model
- `MMAudioSampler` [MMAudio] — in: mmaudio_model:MMAUDIO_MODEL, feature_utils:MMAUDIO_FEATUREUTILS, duration:FLOAT, steps:INT, cfg:FLOAT, seed:INT, prompt:STRING, negative_prompt:STRING, mask_away_clip:BOOLEAN, force_offload:BOOLEAN | out: audio

## Masquerade Nodes
- `Image To Mask` [Masquerade Nodes] — in: image:IMAGE, method=«intensity» | out: MASK

## Meeeyo
- `ProcessString` [Meeeyo/String] — in: input_string:STRING, option=«不改变» | out: STRING
- `TextConcatenator` [Meeeyo/String] — in: - | out: STRING
- `TextToList` [Meeeyo/String] — in: text:STRING, delimiter:STRING | out: STRING

## Mel-Band RoFormer
- `MelBandRoFormerModelLoader` [Mel-Band RoFormer] — in: model_name=«Chroma1/Chroma1-HD-fp8_scaled_rev2.safetensors» | out: model
- `MelBandRoFormerSampler` [Mel-Band RoFormer] — in: model:MELROFORMERMODEL, audio:AUDIO | out: vocals, instruments

## Memory Management
- `RAMCleanup` [Memory Management] — in: clean_file_cache:BOOLEAN, clean_processes:BOOLEAN, clean_dlls:BOOLEAN, retry_times:INT | out: output
- `VRAMCleanup` [Memory Management] — in: offload_model:BOOLEAN, offload_cache:BOOLEAN | out: output

## MiniMax H3
- `SenseNovaH3DistilledBridge` [MiniMax H3/Semantic Bridge] — in: conditioning:CONDITIONING, distilled_adapter=«BUNNY_H3_ActionLogic_Bridge_V1_T8_Compat.safetensors», alpha:FLOAT, magnitude_match=«per_token» | out: conditioning

## PyramidFlowWrapper
- `GIMMVFI_interpolate` [PyramidFlowWrapper] — in: gimmvfi_model:GIMMVIF_MODEL, images:IMAGE, ds_factor:FLOAT, interpolation_factor:INT, seed:INT | out: images, flow_tensors

## Qwen3TTS
- `TDQwen3TTSModelLoader` [Qwen3TTS] — in: model_path=«Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice», precision=«bf16», device=«cuda», attn_implementation=«sdpa», auto_download:BOOLEAN, download_source=«ModelScope» | out: model
- `TDQwen3TTSVoiceClone` [Qwen3TTS] — in: model:QWEN3_TTS_MODEL, text:STRING, ref_audio:AUDIO, language=«Auto» | out: audio
- `TDQwen3TTSVoiceDesign` [Qwen3TTS] — in: model:QWEN3_TTS_MODEL, text:STRING, instruct:STRING, language=«Auto» | out: audio

## RES4LYF
- `ClownsharKSampler_Beta` [RES4LYF/samplers] — in: eta:FLOAT, sampler_name=«multistep/res_2m», scheduler=«beta57», steps:INT, steps_to_run:INT, denoise:FLOAT, cfg:FLOAT, seed:INT, sampler_mode=«standard», bongmath:BOOLEAN | out: output, denoised, options
- `SharkOptions_Beta` [RES4LYF/sampler_options] — in: noise_type_init=«gaussian», s_noise_init:FLOAT, denoise_alt:FLOAT, channelwise_cfg:BOOLEAN | out: options

## Raylight
- `RayBasicGuider` [Raylight/extra/custom_sampling/guiders] — in: ray_actors:RAY_ACTORS, conditioning:CONDITIONING | out: guider
- `RayBasicScheduler` [Raylight/extra/custom_sampling/schedulers] — in: ray_actors:RAY_ACTORS, scheduler=«simple», steps:INT, denoise:FLOAT | out: SIGMAS
- `RayInitializer` [Raylight] — in: ray_cluster_address:STRING, ray_cluster_namespace:STRING, GPU:INT, ulysses_degree:INT, ring_degree:INT, cfg_degree:INT, dp_degree:INT, sync_ulysses:BOOLEAN, clear_vram_after_sampling:BOOLEAN, FSDP:BOOLEAN, FSDP_CPU_OF… | out: ray_actors_init
- `RayInitializerAdvanced` [Raylight] — in: ray_cluster_address:STRING, ray_cluster_namespace:STRING, GPU:INT, GPU_SELECT:STRING, ulysses_degree:INT, ring_degree:INT, clear_vram_after_sampling:BOOLEAN, cfg_degree:INT, dp_degree:INT, sync_ulysses:BOOLEAN, FSDP:B… | out: ray_actors_init
- `RayLoraLoader` [Raylight] — in: lora_name=«Aura_Phantasy_illu.safetensors», strength_model:FLOAT | out: ray_lora
- `RayMiniMaxH3SigmaShift` [Raylight/extra] — in: ray_actors:RAY_ACTORS, shift_video:FLOAT, shift_audio:FLOAT | out: ray_actors
- `RayUNETLoader` [Raylight] — in: unet_name=«Chroma1/Chroma1-HD-fp8_scaled_rev2.safetensors», weight_dtype=«default», ray_actors_init:RAY_ACTORS_INIT | out: ray_actors
- `XFuserSamplerCustomAdvanced` [Raylight/extra/custom_sampling/samplers] — in: add_noise:BOOLEAN, noise_seed:INT, guider:RAY_GUIDER, sampler:SAMPLER, sigmas:SIGMAS, latent_image:LATENT | out: output, denoised_output, ray_actors

## SCAIL-2
- `SCAIL2AlignReferenceFaceToCrop` [SCAIL-2/Scheduled/Face Detail] — in: face_crop_video:IMAGE, reference_image:IMAGE, target_frame_index:INT, face_scale:FLOAT, x_offset_ratio:FLOAT, y_offset_ratio:FLOAT, face_size_basis=«bbox_width», target_face_select=«center», reference_face_select=«lar… | out: aligned_reference_image, debug_preview, summary
- `SCAIL2ChunkKeyframeExtractor` [SCAIL-2/Scheduled/Chunk Plan] — in: video:IMAGE, mode=«planner_summary», max_chunk_frames:INT, overlap_frames:INT, max_frames:INT, include_final_anchor:BOOLEAN, contact_sheet_columns:INT, contact_sheet_thumbnail_width:INT, boundary_anchor_mode=«overlap_… | out: boundary_anchor_frames, new_chunk_start_frames, paired_keyframes, contact_sheet, summary
- `SCAIL2FaceCompositeBack` [SCAIL-2/Scheduled/Face Detail] — in: full_body_video:IMAGE, refined_face_video:IMAGE, crop_masks:MASK, crop_manifest:STRING, feather_px:INT, mask_contract_px:INT, color_correction:BOOLEAN, color_match_method=«local_mean_std», face_fit_mode=«center_crop»,… | out: frames, summary, debug_preview
- `SCAIL2HeadTrackCrop` [SCAIL-2/Scheduled/Face Detail] — in: full_body_video:IMAGE, crop_padding_ratio:FLOAT, square_align:INT, temporal_smoothing:FLOAT, mask_expand_px:INT, mask_blur_px:INT, sam_detection_threshold:FLOAT, sam_max_objects:INT, sam_detect_interval:INT, crop_mode… | out: face_crop_video, crop_masks, crop_manifest, debug_preview
- `SCAIL2KeyframeMatrixViewer` [SCAIL-2/Scheduled/Chunk Plan] — in: paired_keyframes:IMAGE, summary:STRING, filename_prefix:STRING, save_location=«temp», display_group=«both» | out: -
- `SCAIL2ScheduledLongVideoWithSAM` [SCAIL-2/Scheduled] — in: model:MODEL, clip:CLIP, vae:VAE, sampler:SAMPLER, sigmas:SIGMAS, clip_vision:CLIP_VISION, pose_video:IMAGE, segment_plan:STRING, seed:INT, cfg:FLOAT, mode=«replacement», max_frames:INT, max_chunk_frames:INT, overlap_f… | out: frames, used_pose_video_mask, used_reference_mask_timeline, summary
- `SCAIL2SegmentPlanBuilder` [SCAIL-2/Scheduled] — in: segment_count:INT, segment_1_frames:INT, segment_1_reference:INT, segment_1_prompt:STRING, segment_1_negative:STRING, segment_1_boundary_overlap:INT, segment_2_frames:INT, segment_2_reference:INT, segment_2_prompt:STR… | out: segment_plan, summary

## SEEDVR2
- `SeedVR2LoadDiTModel` [SEEDVR2] — in: model=«seedvr2_ema_3b_fp8_e4m3fn.safetensors», device=«cuda:0» | out: SEEDVR2_DIT
- `SeedVR2LoadVAEModel` [SEEDVR2] — in: model=«ema_vae_fp16.safetensors», device=«cuda:0» | out: SEEDVR2_VAE
- `SeedVR2TorchCompileSettings` [SEEDVR2] — in: backend=«inductor», mode=«default», fullgraph:BOOLEAN, dynamic:BOOLEAN, dynamo_cache_size_limit:INT, dynamo_recompile_limit:INT | out: TORCH_COMPILE_ARGS
- `SeedVR2VideoUpscaler` [SEEDVR2] — in: image:IMAGE, dit:SEEDVR2_DIT, vae:SEEDVR2_VAE, seed:INT, resolution:INT, max_resolution:INT, batch_size:INT, uniform_batch_size:BOOLEAN, color_correction=«lab» | out: IMAGE

## T8
- `MiniMaxH3AVDecodeT8` [T8/MiniMax H3/Audio] — in: av_latent:LATENT, video_vae:VAE, audio_vae:VAE | out: frames, generated_audio, video_latent, audio_latent
- `MiniMaxH3AudioConditioningT8` [T8/MiniMax H3/Audio] — in: clip:CLIP, video_vae:VAE, audio_vae:VAE, prompt:STRING, width:INT, height:INT, length:INT, task_type=«auto», audio_mode=«lock_source», audio_denoise_strength:FLOAT, add_source_as_reference:BOOLEAN, prompt_primary_audi… | out: positive, av_latent, mux_audio, conditioned_prompt, media_map_json, report
- `MiniMaxH3ChunkFeedForwardT8Advanced` [T8/MiniMax H3/Models/Experimental] — in: model:MODEL, chunks:INT, seq_threshold:INT | out: model, report_json
- `MiniMaxH3DualClockSamplerT8` [T8/MiniMax H3/Audio] — in: model:MODEL, av_latent:LATENT, steps:INT, shift_video:FLOAT, shift_audio:FLOAT | out: model, sampler, sigmas
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` [T8/MiniMax H3/Latent/Experimental] — in: av_latent:LATENT, model_name=«h3_clean_latent_upscaler_film_epoch200.safetensors», size_mode=«scale_by», scale_by:FLOAT, target_megapixels:FLOAT, target_width:INT, target_height:INT, aspect_policy=«preserve_source», m… | out: av_latent, width, height, report_json
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` [T8/MiniMax H3/Latent/Experimental] — in: model:MODEL, base_steps:INT, coarse_steps:INT, refine_steps:INT | out: coarse_sigmas, refine_sigmas, report_json
- `MiniMaxH3PromptEnhancerT8` [T8/MiniMax H3] — in: prompt:STRING, task_type=«T2VA（文生音视频）», duration_seconds:INT, shot_count=«AUTO（系统自动判断）», rewrite_mode=«balanced», description_word_target:INT, output_language=«中文», prompt_mode=«官方增强», official_skill_profile=«现有兼容（保留中… | out: enhanced_prompt, global_prompt, local_prompts, time_ranges, relay_length, relay_report
- `MiniMaxH3SemanticBridgeApplyT8` [T8/MiniMax H3/Semantic Bridge] — in: conditioning:CONDITIONING, semantic_bridge:T8_SEMANTIC_BRIDGE | out: conditioning, report_json
- `MiniMaxH3SemanticBridgeConfigT8` [T8/MiniMax H3/Semantic Bridge] — in: model_name=«BUNNY_H3_ActionLogic_Bridge_V1_T8_Compat.safetensors», enabled:BOOLEAN, alpha:FLOAT, magnitude_match=«per_token», token_scope=«all_tokens», device=«auto», chunk_tokens:INT | out: semantic_bridge, report_json
- `MiniMaxH3TwoPassDetailMixerT8Advanced` [T8/MiniMax H3/Quality/Experimental] — in: model:MODEL, av_latent:LATENT, refine_sigmas:SIGMAS, shift_video:FLOAT, shift_audio:FLOAT, enable_tail:BOOLEAN, extra_tail_steps:INT, tail_spacing=«video_sigma_linear», enable_model_time_bias:BOOLEAN, bias:FLOAT, bias… | out: model, sampler, sigmas, actual_nfe, planned_joint_av_forwards, report_json
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` [T8/MiniMax H3/Latent/Experimental] — in: learned_latent:LATENT, highres_template:LATENT, positive:CONDITIONING, audio_policy=«auto» | out: av_latent, positive, report_json
- `MiniMaxH3VDNExecutionPlanT8Advanced` [T8/MiniMax H3/Performance/Advanced] — in: model:MODEL, av_latent:LATENT | out: model, sampler, sigmas, report_json
- `MiniMaxH3VDNModelComposerT8Advanced` [T8/MiniMax H3/Performance/Advanced] — in: model:MODEL, vdn_root=«OpenVDN/vdn-minimax-h3», stage=«stage_dmd_8nfe», verify_hashes:BOOLEAN, allow_structural_base:BOOLEAN | out: model, report_json

## TTP
- `TTP_Image_Assy` [TTP/Image] — in: tiles:IMAGE, positions:LIST, original_size:TUPLE, grid_size:TUPLE, padding:INT | out: RECONSTRUCTED_IMAGE
- `TTP_Image_Tile_Batch` [TTP/Image] — in: image:IMAGE, tile_width:INT, tile_height:INT | out: IMAGES, POSITIONS, ORIGINAL_SIZE, GRID_SIZE
- `TTP_Tile_image_size` [TTP/Image] — in: image:IMAGE, width_factor:INT, height_factor:INT, overlap_rate:FLOAT | out: tile_width, tile_height

## VRAM
- `PainterVRAM` [VRAM] — in: reserved:FLOAT, mode=«auto», clean_gpu_before:BOOLEAN, auto_max:FLOAT, seed:INT | out: output, reserved_gb
- `ReservedVRAMSetter` [VRAM] — in: reserved:FLOAT, mode=«auto», seed:INT, auto_max_reserved:FLOAT, clean_gpu_before:BOOLEAN | out: output, SEED, Reserved(GB)

## Video Helper Suite 🎥🅥🅗🅢
- `VHS_LoadAudioUpload` [Video Helper Suite 🎥🅥🅗🅢/audio] — in: audio=«1.mp3» | out: audio, duration
- `VHS_LoadVideo` [Video Helper Suite 🎥🅥🅗🅢] — in: video=«1741106068055975465.mp4», force_rate:FLOAT, custom_width:INT, custom_height:INT, frame_load_cap:INT, skip_first_frames:INT, select_every_nth:INT | out: IMAGE, frame_count, audio, video_info
- `VHS_LoadVideoFFmpeg` [Video Helper Suite 🎥🅥🅗🅢] — in: video=«1741106068055975465.mp4», force_rate:FLOAT, custom_width:INT, custom_height:INT, frame_load_cap:INT, start_time:FLOAT | out: IMAGE, mask, audio, video_info
- `VHS_SplitImages` [Video Helper Suite 🎥🅥🅗🅢/image] — in: images:IMAGE, split_index:INT | out: IMAGE_A, A_count, IMAGE_B, B_count
- `VHS_VideoCombine` [Video Helper Suite 🎥🅥🅗🅢] — in: images:IMAGE, frame_rate:FLOAT, loop_count:INT, filename_prefix:STRING, format=«image/gif», pingpong:BOOLEAN, save_output:BOOLEAN | out: Filenames
- `VHS_VideoInfo` [Video Helper Suite 🎥🅥🅗🅢] — in: video_info:VHS_VIDEOINFO | out: source_fps🟨, source_frame_count🟨, source_duration🟨, source_width🟨, source_height🟨, loaded_fps🟦, loaded_frame_count🟦, loaded_duration🟦, loaded_width🟦, loaded_height🟦
- `VHS_VideoInfoLoaded` [Video Helper Suite 🎥🅥🅗🅢] — in: video_info:VHS_VIDEOINFO | out: fps🟦, frame_count🟦, duration🟦, width🟦, height🟦

## Viggle Remake
- `RemakeConditioning` [Viggle Remake] — in: clip:CLIP, vae:VAE, audio_vae:VAE, source:IMAGE, prompt:STRING, ref_1:IMAGE, pins:STRING, frames:INT, short_edge:INT | out: positive, latent
- `RemakeKeyframeUntil` [Viggle Remake] — in: model:MODEL, keyframe_until:FLOAT | out: MODEL
- `RemakeNoise` [Viggle Remake] — in: positive:CONDITIONING, seed:INT | out: NOISE

## WAS Suite
- `Load Image Batch` [WAS Suite/IO] — in: mode=«single_image», seed:INT, index:INT, label:STRING, path:STRING, pattern:STRING, allow_RGBA_output=«false» | out: image, filename_text
- `Lora Loader` [WAS Suite/Loaders] — in: model:MODEL, clip:CLIP, lora_name=«None», strength_model:FLOAT, strength_clip:FLOAT | out: MODEL, CLIP, NAME_STRING
- `Text Concatenate` [WAS Suite/Text] — in: delimiter:STRING, clean_whitespace=«true» | out: STRING
- `Text Load Line From File` [WAS Suite/Text] — in: file_path:STRING, dictionary_name:STRING, label:STRING, mode=«automatic», index:INT | out: line_text, dictionary
- `Text Multiline` [WAS Suite/Text] — in: text:STRING | out: STRING
- `Text String` [WAS Suite/Text] — in: text:STRING | out: TEXT, TEXT_B, TEXT_C, TEXT_D

## Wan2.2
- `Wan22PromptSelector` [Wan2.2/提示词生成] — in: 场景类型=«——», 运动场景=«——», 人物情绪=«——», 运镜方式=«——», 光源类型=«——», 光线类型=«——», 镜头类型=«——», 焦距=«——», 色调=«——», 视觉风格=«——», 特效镜头=«——» | out: 提示词

## WanAnimatePreprocess
- `DrawViTPose` [WanAnimatePreprocess] — in: pose_data:POSEDATA, width:INT, height:INT, retarget_padding:INT, body_stick_width:INT, hand_stick_width:INT, draw_head:BOOLEAN | out: pose_images
- `OnnxDetectionModelLoader` [WanAnimatePreprocess] — in: vitpose_model=«vitpose-l-wholebody.onnx», yolo_model=«vitpose-l-wholebody.onnx», onnx_device=«CUDAExecutionProvider» | out: model
- `PoseAndFaceDetection` [WanAnimatePreprocess] — in: model:POSEMODEL, images:IMAGE, width:INT, height:INT | out: pose_data, face_images, key_frame_body_points, bboxes, face_bboxes

## WanVideoWrapper
- `CreateCFGScheduleFloatList` [WanVideoWrapper] — in: steps:INT, cfg_scale_start:FLOAT, cfg_scale_end:FLOAT, interpolation=«linear», start_percent:FLOAT, end_percent:FLOAT | out: float_list
- `DownloadAndLoadWav2VecModel` [WanVideoWrapper] — in: model=«TencentGameMate/chinese-wav2vec2-base», base_precision=«fp16», load_device=«main_device» | out: wav2vec_model
- `LoadWanVideoClipTextEncoder` [WanVideoWrapper] — in: model_name=«CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors», precision=«fp16» | out: wan_clip_vision
- `LoadWanVideoT5TextEncoder` [WanVideoWrapper] — in: model_name=«Qwen3-VL-32B-Instruct-layer50_quanto_bf16_int8.safetensors», precision=«bf16» | out: wan_t5_model
- `MultiTalkModelLoader` [WanVideoWrapper] — in: model=«FireRed/FireRed-Image-Edit-1.1-transformer-q4_1.gguf» | out: model
- `MultiTalkWav2VecEmbeds` [WanVideoWrapper] — in: wav2vec_model:WAV2VECMODEL, audio_1:AUDIO, normalize_loudness:BOOLEAN, num_frames:INT, fps:FLOAT, audio_scale:FLOAT, audio_cfg_scale:FLOAT, multi_audio_type=«para» | out: multitalk_embeds, audio, num_frames
- `WanVideoAnimateEmbeds` [WanVideoWrapper] — in: vae:WANVAE, width:INT, height:INT, num_frames:INT, force_offload:BOOLEAN, frame_window_size:INT, colormatch=«disabled», pose_strength:FLOAT, face_strength:FLOAT | out: image_embeds
- `WanVideoBlockSwap` [WanVideoWrapper] — in: blocks_to_swap:INT, offload_img_emb:BOOLEAN, offload_txt_emb:BOOLEAN | out: block_swap_args
- `WanVideoClipVisionEncode` [WanVideoWrapper] — in: clip_vision:CLIP_VISION, image_1:IMAGE, strength_1:FLOAT, strength_2:FLOAT, crop=«center», combine_embeds=«average», force_offload:BOOLEAN | out: image_embeds
- `WanVideoContextOptions` [WanVideoWrapper] — in: context_schedule=«uniform_standard», context_frames:INT, context_stride:INT, context_overlap:INT, freenoise:BOOLEAN, verbose:BOOLEAN | out: context_options
- `WanVideoDecode` [WanVideoWrapper] — in: vae:WANVAE, samples:LATENT, enable_vae_tiling:BOOLEAN, tile_x:INT, tile_y:INT, tile_stride_x:INT, tile_stride_y:INT | out: images
- `WanVideoEncode` [WanVideoWrapper] — in: vae:WANVAE, image:IMAGE, enable_vae_tiling:BOOLEAN, tile_x:INT, tile_y:INT, tile_stride_x:INT, tile_stride_y:INT | out: samples
- `WanVideoImageToVideoEncode` [WanVideoWrapper] — in: width:INT, height:INT, num_frames:INT, noise_aug_strength:FLOAT, start_latent_strength:FLOAT, end_latent_strength:FLOAT, force_offload:BOOLEAN | out: image_embeds
- `WanVideoImageToVideoMultiTalk` [WanVideoWrapper] — in: vae:WANVAE, width:INT, height:INT, frame_window_size:INT, motion_frame:INT, force_offload:BOOLEAN, colormatch=«disabled» | out: image_embeds, output_path
- `WanVideoLoraSelect` [WanVideoWrapper] — in: lora=«Aura_Phantasy_illu.safetensors», strength:FLOAT | out: lora
- `WanVideoLoraSelectMulti` [WanVideoWrapper] — in: lora_0=«none», strength_0:FLOAT, lora_1=«none», strength_1:FLOAT, lora_2=«none», strength_2:FLOAT, lora_3=«none», strength_3:FLOAT, lora_4=«none», strength_4:FLOAT | out: lora
- `WanVideoModelLoader` [WanVideoWrapper] — in: model=«FireRed/FireRed-Image-Edit-1.1-transformer-q4_1.gguf», base_precision=«bf16», quantization=«disabled», load_device=«offload_device» | out: model
- `WanVideoSLG` [WanVideoWrapper] — in: blocks:STRING, start_percent:FLOAT, end_percent:FLOAT | out: slg_args
- `WanVideoSampler` [WanVideoWrapper] — in: model:WANVIDEOMODEL, image_embeds:WANVIDIMAGE_EMBEDS, steps:INT, cfg:FLOAT, shift:FLOAT, seed:INT, force_offload:BOOLEAN, scheduler=«unipc», riflex_freq_index:INT | out: samples, denoised_samples
- `WanVideoSetBlockSwap` [WanVideoWrapper] — in: model:WANVIDEOMODEL | out: model
- `WanVideoSetLoRAs` [WanVideoWrapper] — in: model:WANVIDEOMODEL | out: model
- `WanVideoTextEncode` [WanVideoWrapper] — in: positive_prompt:STRING, negative_prompt:STRING | out: text_embeds
- `WanVideoTextEncodeCached` [WanVideoWrapper] — in: model_name=«Qwen3-VL-32B-Instruct-layer50_quanto_bf16_int8.safetensors», precision=«bf16», positive_prompt:STRING, negative_prompt:STRING, quantization=«disabled», use_disk_cache:BOOLEAN, device=«gpu» | out: text_embeds, negative_text_embeds, positive_prompt
- `WanVideoTorchCompileSettings` [WanVideoWrapper] — in: backend=«inductor», fullgraph:BOOLEAN, mode=«default», dynamic:BOOLEAN, dynamo_cache_size_limit:INT, compile_transformer_blocks_only:BOOLEAN | out: torch_compile_args
- `WanVideoVAELoader` [WanVideoWrapper] — in: model_name=«Krea2-HD-vae.safetensors» | out: vae

## WhatDreamsCost
- `LTXSequencer` [WhatDreamsCost] — in: positive:CONDITIONING, negative:CONDITIONING, vae:VAE, latent:LATENT, multi_input:IMAGE, num_images:INT, insert_mode=«frames», frame_rate:INT | out: positive, negative, latent
- `MultiImageLoader` [WhatDreamsCost] — in: image_paths:STRING, width:INT, height:INT, interpolation=«lanczos», resize_method=«keep proportion», multiple_of:INT, img_compression:INT | out: multi_output, image_1, image_2, image_3, image_4, image_5, image_6, image_7, image_8, image_9, image_10, image_11, image_12, image_13, image_14, image_15, image_16, image_17, image_18, image_19, image_20, image_21, image_22, image_23, image_24, image_25, image_26, image_27, image_28, image_29, image_30, image_31, image_32, image_33, image_34, image_35, image_36, image_37, image_38, image_39, image_40, image_41, image_42, image_43, image_44, image_45, image_46, image_47, image_48, image_49, image_50

## YCNodes-MiniMax-H3
- `H3SigmaRefiner` [YCNodes-MiniMax-H3/scheduler] — in: sigmas:SIGMAS, extra_steps:INT, start_at_sigma:FLOAT, end_at_sigma:FLOAT, spacing=«cosine» | out: sigmas

## Zealman
- `GIMMVFI_stream` [Zealman] — in: gimmvfi_model:GIMMVIF_MODEL, video:VIDEO, interpolation_factor:FLOAT, window_frames:INT, ds_factor:FLOAT, seed:INT | out: saved_path
- `ZealmanH3LoadImageToRefImages` [Zealman/H3] — in: fps:FLOAT, video_trim_seconds:FLOAT, audio_trim_seconds:FLOAT, image_max_side:INT, video_max_side:INT | out: ref_images, image_list, ref_videos, ref_video_audios, ref_audios
- `ZealmanH3ModelLoader` [Zealman/H3] — in: unet_name=«minimax/minimax_h3_fl2va_pruned_int8_convrot.safetensors», weight_dtype=«default», clip_name=«qwen3vl_32b_minimax_h3_int8_convrot.safetensors», clip_device=«default», video_vae=«minimax_h3_video_vae_fp16.sa… | out: model, clip, video_vae, audio_vae
- `ZealmanH3PickReferenceMedia` [Zealman/H3] — in: fps:FLOAT, video_trim_seconds=«auto», audio_trim_seconds=«auto», image_max_side=«auto», video_max_side=«auto», prompt:STRING, seconds:INT, aspect_ratio=«1:1 (Square)», megapixels:FLOAT, multiple:INT | out: ref_image_0, ref_image_1, ref_image_2, ref_image_3, ref_image_4, ref_image_5, ref_image_6, ref_image_7, ref_image_8, ref_video_0, ref_video_1, ref_video_2, ref_video_audio_0, ref_video_audio_1, ref_video_audio_2, ref_audio_0, ref_audio_1, ref_audio_2, prompt, width, height, length, seconds
- `ZealmanLLM_Generate` [Zealman/LLM] — in: zealman模型:ZEALMANLLM, 提示词:STRING, 系统提示词:STRING, 最大边长:INT, 最大生成token:INT, 温度:FLOAT, top_p:FLOAT, top_k:INT, seed:INT, 输出think块:BOOLEAN, 生成后自动卸载:BOOLEAN | out: result
- `ZealmanLLM_H3Prompt` [Zealman/LLM] — in: zealman模型:ZEALMANLLM, 提示词:STRING, 技能=«auto», 时长:FLOAT, 启用思考:BOOLEAN, 推理强度=«medium», seed:INT, 最大生成token:INT, 每秒抽帧:INT, 生成后自动卸载:BOOLEAN | out: 提示词, 技能, 模式
- `ZealmanLLM_ModelLoader` [Zealman/LLM] — in: 模型系列=«Qwen3.8-VL», 主模型=«Qwen3.8-27B-Q4_K_M.gguf», 视觉投影mmproj=«Qwen3.8-mmproj-BF16.gguf», 启用思考:BOOLEAN, 保留历史think:BOOLEAN, 上下文长度:INT, GPU层数:INT, KV缓存K类型=«默认(F16)», KV缓存V类型=«默认(F16)», Qwen3.8推理强度=«xhigh», MoE专家上CPU:BOOL… | out: zealman模型
- `ZealmanVideoOutput` [Zealman] — in: images:IMAGE, frame_rate:FLOAT, filename_prefix:STRING, save_output:BOOLEAN | out: saved_path

## advanced
- `CFGNorm` [advanced/guidance] — in: model:MODEL, strength:FLOAT | out: patched_model
- `CFGZeroStar` [advanced/guidance] — in: model:MODEL | out: patched_model
- `EasyCache` [advanced/debug] — in: model:MODEL, reuse_threshold:FLOAT, start_percent:FLOAT, end_percent:FLOAT, verbose:BOOLEAN | out: MODEL
- `Flux2KleinEditTextEncode_EditUtils` [advanced/conditioning] — in: clip:CLIP, vae:VAE, prompt:STRING | out: conditioning, latent, custom_output, main_image, mask

## audio
- `AudioCrop` [audio] — in: audio:AUDIO, start_time:STRING, end_time:STRING | out: AUDIO
- `AudioSeparation` [audio] — in: audio:AUDIO | out: Bass, Drums, Other, Vocals
- `LoadAudio` [audio] — in: audio=«1.mp3» | out: AUDIO
- `PreviewAudio` [audio] — in: audio:AUDIO | out: audio
- `SaveAudio` [audio] — in: audio:AUDIO, filename_prefix:STRING | out: audio
- `SaveAudioAdvanced` [audio] — in: audio:AUDIO, filename_prefix:STRING, format:COMFY_DYNAMICCOMBO_V3 | out: audio
- `SaveAudioMP3` [audio] — in: audio:AUDIO, filename_prefix:STRING, quality=«V0» | out: audio
- `TrimAudioDuration` [audio] — in: audio:AUDIO, start_index:FLOAT, duration:FLOAT | out: AUDIO

## bootleg
- `CLIPLoaderGGUF` [bootleg] — in: clip_name=«Qwen3-4b-Z-Image-Engineer-V4-Q8_0.gguf», type=«stable_diffusion» | out: CLIP
- `UnetLoaderGGUF` [bootleg] — in: unet_name=«FireRed/FireRed-Image-Edit-1.1-transformer-q4_1.gguf» | out: MODEL

## conditioning
- `BNK_CLIPTextEncodeAdvanced` [conditioning/advanced] — in: text:STRING, clip:CLIP, token_normalization=«none», weight_interpretation=«comfy» | out: CONDITIONING
- `LTXVImgToVideoConditionOnly` [conditioning/video_models] — in: vae:VAE, image:IMAGE, latent:LATENT, strength:FLOAT | out: latent
- `PromptRelaySmartEncode` [conditioning/prompt_relay] — in: model:MODEL, clip:CLIP, latent:LATENT, global_prompt:STRING, smart_prompt:STRING, normalize_by_tokens:BOOLEAN, epsilon:FLOAT | out: model, positive

## crystools 🪛
- `Switch any [Crystools]` [crystools 🪛/Switch] — in: on_true:*, on_false:*, boolean:BOOLEAN | out: *
- `Switch image [Crystools]` [crystools 🪛/Switch] — in: on_true:IMAGE, on_false:IMAGE, boolean:BOOLEAN | out: image

## essentials
- `BatchCount+` [essentials/utilities] — in: batch:* | out: INT
- `GetImageSize+` [essentials/image utils] — in: image:IMAGE | out: width, height, count
- `ImageFromBatch+` [essentials/image batch] — in: image:IMAGE, start:INT, length:INT | out: IMAGE
- `ImageSmartSharpen+` [essentials/image processing] — in: image:IMAGE, noise_radius:INT, preserve_edges:FLOAT, sharpen:FLOAT, ratio:FLOAT | out: IMAGE
- `MaskPreview+` [essentials/mask] — in: mask:MASK | out: images
- `SimpleMath+` [essentials/utilities] — in: value:STRING | out: INT, FLOAT
- `SimpleMathDual+` [essentials/utilities] — in: value_1:STRING, value_2:STRING | out: int_1, float_1, int_2, float_2

## everywhere
- `Anything Everywhere` [everywhere] — in: - | out: -

## image
- `BatchImagesNode` [image/batch] — in: images:COMFY_AUTOGROW_V3 | out: IMAGE
- `ColoristFilmGrain` [image/postprocessing] — in: image:IMAGE, grain_size:FLOAT, strength:FLOAT, shadow_bias:FLOAT, luma_amt:FLOAT, chroma_amt:FLOAT, blend_mode=«add», seed:INT, grain_motion:FLOAT | out: image
- `ColoristHalation` [image/postprocessing] — in: image:IMAGE, threshold:FLOAT, strength:FLOAT, radius:FLOAT | out: image
- `GetImageSize` [image] — in: image:IMAGE | out: width, height, batch_size
- `GrowMask` [image/mask] — in: mask:MASK, expand:INT, tapered_corners:BOOLEAN | out: MASK
- `ImageBatch` [image/batch] — in: image1:IMAGE, image2:IMAGE | out: IMAGE
- `ImageCompare` [image] — in: compare_view:IMAGECOMPARE | out: -
- `ImageCompositeMasked` [image/compositing] — in: destination:IMAGE, source:IMAGE, x:INT, y:INT, resize_source:BOOLEAN | out: IMAGE
- `ImageFromBatch` [image/batch] — in: image:IMAGE, batch_index:INT, length:INT | out: IMAGE
- `ImageScale` [image/upscaling] — in: image:IMAGE, upscale_method=«nearest-exact», width:INT, height:INT, crop=«disabled» | out: IMAGE
- `ImageScaleBy` [image/upscaling] — in: image:IMAGE, upscale_method=«nearest-exact», scale_by:FLOAT | out: IMAGE
- `ImageScaleToTotalPixels` [image/upscaling] — in: image:IMAGE, upscale_method=«nearest-exact», megapixels:FLOAT, resolution_steps:INT | out: IMAGE
- `ImageScaleToTotalPixelsX` [image/upscaling] — in: image:IMAGE, megapixels:FLOAT, multiple_of:INT, resize_mode=«crop», upscale_method=«lanczos» | out: image, width, height
- `ImageSharpen` [image/filters] — in: image:IMAGE, sharpen_radius:INT, sigma:FLOAT, alpha:FLOAT | out: IMAGE
- `ImageUpscaleWithModel` [image/upscaling] — in: upscale_model:UPSCALE_MODEL, image:IMAGE | out: IMAGE
- `LoadImage` [image] — in: image=«005.jpg» | out: IMAGE, MASK
- `LoadImageMask` [image] — in: image=«005.jpg», channel=«alpha» | out: MASK
- `MaskComposite` [image/mask] — in: destination:MASK, source:MASK, x:INT, y:INT, operation=«multiply» | out: MASK
- `MaskToImage` [image/mask] — in: mask:MASK | out: IMAGE
- `PreviewImage` [image] — in: images:IMAGE | out: images
- `RIFEInterpolation` [image/animation] — in: images:IMAGE, source_fps:FLOAT, target_fps:FLOAT, scale:FLOAT | out: images
- `RTXVideoSuperResolution` [image/upscaling] — in: images:IMAGE, resize_type:COMFY_DYNAMICCOMBO_V3, quality=«ULTRA» | out: upscaled_images
- `RepeatImageBatch` [image/batch] — in: image:IMAGE, amount:INT | out: IMAGE
- `ResizeImageMaskNode` [image/transform] — in: input:COMFY_MATCHTYPE_V3, resize_type:COMFY_DYNAMICCOMBO_V3, scale_method=«area» | out: resized
- `ResizeImagesByLongerEdge` [image/transform] — in: images:IMAGE, longer_edge:INT | out: images
- `ResizeShortestToNode` [image] — in: image:IMAGE, size:INT, method=«NEAREST» | out: IMAGE
- `SaveImage` [image] — in: images:IMAGE, filename_prefix:STRING | out: images
- `SaveImageAdvanced` [image] — in: images:IMAGE, filename_prefix:STRING, format:COMFY_DYNAMICCOMBO_V3 | out: images
- `SolidMask` [image/mask] — in: value:FLOAT, width:INT, height:INT | out: MASK
- `UltimateSDUpscale` [image/upscaling] — in: image:IMAGE, model:MODEL, positive:CONDITIONING, negative:CONDITIONING, vae:VAE, upscale_by:FLOAT, seed:INT, steps:INT, cfg:FLOAT, sampler_name=«euler», scheduler=«simple», denoise:FLOAT, upscale_model:UPSCALE_MODEL, … | out: IMAGE
- `VOSR2ModelLoader` [image/upscaling/VOSR2] — in: model=«VOSR2», dtype=«default» | out: model
- `VOSR2Upscale` [image/upscaling/VOSR2] — in: model:VOSR2_MODEL, image:IMAGE, upscale:INT, seed:INT, color_alignment=«wavelet», tile_size:INT, tile_overlap:INT, vae_tile_size:INT, vae_tile_overlap:INT | out: IMAGE
- `WD14Tagger|pysssss` [image] — in: image:IMAGE, model=«wd-v1-4-moat-tagger-v2», threshold:FLOAT, character_threshold:FLOAT, replace_underscore:BOOLEAN, trailing_comma:BOOLEAN, exclude_tags:STRING | out: STRING
- `WJIDehaze` [image/color_correction] — in: 图像:IMAGE, 暗部裁剪:FLOAT, 亮部裁剪:FLOAT, 强度:FLOAT | out: 去灰结果
- `WJIFrequencyMixer` [image/frequency_separation] — in: 高频层混合模式=«线性光», 低频层透明度:FLOAT, 高频层透明度:FLOAT | out: 合成结果
- `WJIFrequencySeparation` [image/frequency_separation] — in: 图像:IMAGE, 模糊半径:INT, 模糊强度:FLOAT, 高频_去色:BOOLEAN | out: 低频层, 高频层, 原图

## inpaint
- `INPAINT_ExpandMask` [inpaint] — in: mask:MASK, grow:INT, blur:INT, blur_type=«gaussian» | out: mask
- `InpaintCropImproved` [inpaint] — in: image:IMAGE, downscale_algorithm=«bilinear», upscale_algorithm=«bicubic», preresize:BOOLEAN, preresize_mode=«ensure minimum resolution», preresize_min_width:INT, preresize_min_height:INT, preresize_max_width:INT, prer… | out: stitcher, cropped_image, cropped_mask
- `InpaintStitchImproved` [inpaint] — in: stitcher:STITCHER, inpainted_image:IMAGE | out: image

## jamesWalker55
- `JWImageResizeByLongerSide` [jamesWalker55] — in: image:IMAGE, size:INT, interpolation_mode=«bicubic» | out: IMAGE

## krea2edit
- `Krea2EditGroundedEncode` [krea2edit] — in: clip:CLIP, prompt:STRING | out: CONDITIONING
- `Krea2EditModelPatch` [krea2edit] — in: model:MODEL, source_latent:LATENT | out: MODEL

## latent
- `MiniMaxH3VAEDecodeFast` [latent/minimax_h3] — in: samples:LATENT, vae:VAE, tiling:BOOLEAN, tile_size:INT, tile_overlap:INT, output_device=«cpu», temporal_tiling:BOOLEAN, temporal_tile_frames:INT, temporal_context_frames:INT, seam_warning_threshold:FLOAT | out: images
- `VSRDecode` [latent] — in: vae:VAE, samples:LATENT, images:IMAGE, detail:FLOAT | out: IMAGE
- `WJILatentPreset` [latent] — in: 预设分辨率=«自定义», 横竖对调:BOOLEAN, 批量大小:INT | out: Latent, 宽, 高, 总张数

## llama-cpp-vlm
- `llama_cpp_instruct_adv` [llama-cpp-vlm] — in: llama_model:LLAMACPPMODEL, preset_prompt=«Normal - Describe», custom_prompt:STRING, system_prompt:STRING, inference_mode=«one by one», max_frames:INT, max_size:INT, seed:INT, force_offload:BOOLEAN, save_states:BOOLEAN | out: output, output_list, state_uid
- `llama_cpp_model_loader` [llama-cpp-vlm] — in: model=«Florence-2-base-PromptGen-v2.0/model.safetensors», mmproj=«None», chat_handler=«None», n_ctx:INT, vram_limit:INT, image_min_tokens:INT, image_max_tokens:INT, load_mtp:BOOLEAN | out: llama_model
- `llama_cpp_parameters` [llama-cpp-vlm] — in: max_tokens:INT, top_k:INT, top_p:FLOAT, min_p:FLOAT, typical_p:FLOAT, temperature:FLOAT, repeat_penalty:FLOAT, frequency_penalty:FLOAT, present_penalty:FLOAT, mirostat_mode:INT, mirostat_eta:FLOAT, mirostat_tau:FLOAT,… | out: parameters

## maoyu
- `AnySwitch` [maoyu/utils] — in: - | out: 是否启用优先, 输出结果

## math
- `CM_FloatBinaryOperation` [math/float] — in: op=«Add», a:FLOAT, b:FLOAT | out: FLOAT
- `CM_FloatToInt` [math/conversion] — in: a:FLOAT | out: INT
- `CM_IntToFloat` [math/conversion] — in: a:INT | out: FLOAT

## model
- `AudioEncoderEncode` [model/conditioning] — in: audio_encoder:AUDIO_ENCODER, audio:AUDIO | out: AUDIO_ENCODER_OUTPUT
- `AudioEncoderLoader` [model/loaders] — in: audio_encoder_name=«sheetsage2_bf16.safetensors» | out: AUDIO_ENCODER
- `BasicGuider` [model/sampling/guiders] — in: model:MODEL, conditioning:CONDITIONING | out: GUIDER
- `BasicScheduler` [model/sampling/schedulers] — in: model:MODEL, scheduler=«simple», steps:INT, denoise:FLOAT | out: SIGMAS
- `BlockSparseAttention` [model/patch] — in: model:MODEL, selection:COMFY_DYNAMICCOMBO_V3, start_percent:FLOAT, end_percent:FLOAT, dense_blocks:STRING, min_tokens:INT, extra_tokens:INT, sink_conditioning=«exact_kv_and_rows», verbose:BOOLEAN | out: model
- `CFGGuider` [model/sampling/guiders] — in: model:MODEL, positive:CONDITIONING, negative:CONDITIONING, cfg:FLOAT | out: GUIDER
- `CLIPLoader` [model/loaders] — in: clip_name=«Qwen3-VL-32B-Instruct-layer50_quanto_bf16_int8.safetensors», type=«stable_diffusion» | out: CLIP
- `CLIPSetLastLayer` [model/conditioning] — in: clip:CLIP, stop_at_clip_layer:INT | out: CLIP
- `CLIPTextEncode` [model/conditioning] — in: text:STRING, clip:CLIP | out: CONDITIONING
- `CLIPTextEncodeFlux` [model/conditioning/flux] — in: clip:CLIP, clip_l:STRING, t5xxl:STRING, guidance:FLOAT | out: CONDITIONING
- `CLIPVisionEncode` [model/conditioning] — in: clip_vision:CLIP_VISION, image:IMAGE, crop=«center» | out: CLIP_VISION_OUTPUT
- `CLIPVisionLoader` [model/loaders] — in: clip_name=«CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors» | out: CLIP_VISION
- `CheckpointLoaderSimple` [model/loaders] — in: ckpt_name=«10Eros_v1-fp8mixed_learned.safetensors» | out: MODEL, CLIP, VAE
- `ConditioningCombine` [model/conditioning/transform] — in: conditioning_1:CONDITIONING, conditioning_2:CONDITIONING | out: CONDITIONING
- `ConditioningSetArea` [model/conditioning/transform] — in: conditioning:CONDITIONING, width:INT, height:INT, x:INT, y:INT, strength:FLOAT | out: CONDITIONING
- `ConditioningZeroOut` [model/conditioning/transform] — in: conditioning:CONDITIONING | out: CONDITIONING
- `ControlNetApplyAdvanced` [model/conditioning/controlnet] — in: positive:CONDITIONING, negative:CONDITIONING, control_net:CONTROL_NET, image:IMAGE, strength:FLOAT, start_percent:FLOAT, end_percent:FLOAT | out: positive, negative
- `ControlNetLoader` [model/loaders] — in: control_net_name=«FLUX.1-dev-ControlNet-Union-Pro-2.0.safetensors» | out: CONTROL_NET
- `DenoMiniMaxH3ReferenceToVideo` [model/conditioning/minimax] — in: clip:CLIP, prompt:STRING, width:INT, height:INT, length:INT, ref_image_size=«match» | out: positive, LATENT
- `DisableNoise` [model/sampling/noise] — in: - | out: NOISE
- `DualCLIPLoader` [model/loaders] — in: clip_name1=«Qwen3-VL-32B-Instruct-layer50_quanto_bf16_int8.safetensors», clip_name2=«Qwen3-VL-32B-Instruct-layer50_quanto_bf16_int8.safetensors», type=«sdxl» | out: CLIP
- `EmptyAceStep1.5LatentAudio` [model/latent/ace] — in: seconds:FLOAT, batch_size:INT | out: LATENT
- `EmptyFlux2LatentImage` [model/latent/flux] — in: width:INT, height:INT, batch_size:INT | out: LATENT
- `EmptyLTXVLatentVideo` [model/latent/ltxv] — in: width:INT, height:INT, length:INT, batch_size:INT | out: LATENT
- `EmptyLatentAudio` [model/latent] — in: seconds:FLOAT, batch_size:INT | out: LATENT
- `EmptyLatentImage` [model/latent] — in: width:INT, height:INT, batch_size:INT | out: LATENT
- `EmptyMiniMaxH3LatentAV` [model/latent/minimax] — in: width:INT, height:INT, length:INT | out: LATENT
- `EmptyMiniMaxMusic3LatentAudio` [model/latent/minimax music] — in: seconds:FLOAT, batch_size:INT | out: LATENT
- `EmptySD3LatentImage` [model/latent/stable diffusion] — in: width:INT, height:INT, batch_size:INT | out: LATENT
- `EmptyYuE2LatentAudio` [model/latent/yue2] — in: seconds:FLOAT, batch_size:INT | out: LATENT
- `ExtendIntermediateSigmas` [model/sampling/sigmas] — in: sigmas:SIGMAS, steps:INT, start_at_sigma:FLOAT, end_at_sigma:FLOAT, spacing=«linear» | out: SIGMAS
- `Flux2Scheduler` [model/sampling/schedulers] — in: steps:INT, width:INT, height:INT | out: SIGMAS
- `FluxKontextImageScale` [model/conditioning/flux] — in: image:IMAGE | out: IMAGE
- `FluxKontextMultiReferenceLatentMethod` [model/conditioning/flux] — in: conditioning:CONDITIONING, reference_latents_method=«offset» | out: CONDITIONING
- `InpaintModelConditioning` [model/conditioning] — in: positive:CONDITIONING, negative:CONDITIONING, vae:VAE, pixels:IMAGE, mask:MASK, noise_mask:BOOLEAN | out: positive, negative, latent
- `KSampler` [model/sampling] — in: model:MODEL, seed:INT, steps:INT, cfg:FLOAT, sampler_name=«euler», scheduler=«simple», positive:CONDITIONING, negative:CONDITIONING, latent_image:LATENT, denoise:FLOAT | out: LATENT
- `KSamplerAdvanced` [model/sampling] — in: model:MODEL, add_noise=«enable», noise_seed:INT, steps:INT, cfg:FLOAT, sampler_name=«euler», scheduler=«simple», positive:CONDITIONING, negative:CONDITIONING, latent_image:LATENT, start_at_step:INT, end_at_step:INT, r… | out: LATENT
- `KSamplerSelect` [model/sampling/samplers] — in: sampler_name=«euler» | out: SAMPLER
- `LTXAVTextEncoderLoader` [model/loaders] — in: text_encoder=«Qwen3-VL-32B-Instruct-layer50_quanto_bf16_int8.safetensors», ckpt_name=«10Eros_v1-fp8mixed_learned.safetensors», device=«default» | out: CLIP
- `LTXVAddGuide` [model/conditioning/ltxv] — in: positive:CONDITIONING, negative:CONDITIONING, vae:VAE, latent:LATENT, image:IMAGE, frame_idx:INT, strength:FLOAT | out: positive, negative, latent
- `LTXVAudioVAEDecode` [model/latent/ltxv] — in: samples:LATENT, audio_vae:VAE | out: Audio
- `LTXVAudioVAEEncode` [model/latent/ltxv] — in: audio:AUDIO, audio_vae:VAE | out: Audio Latent
- `LTXVAudioVAELoader` [model/loaders] — in: ckpt_name=«10Eros_v1-fp8mixed_learned.safetensors» | out: Audio VAE
- `LTXVConcatAVLatent` [model/latent/ltxv] — in: video_latent:LATENT, audio_latent:LATENT | out: latent
- `LTXVConditioning` [model/conditioning/ltxv] — in: positive:CONDITIONING, negative:CONDITIONING, frame_rate:FLOAT | out: positive, negative
- `LTXVCropGuides` [model/conditioning/ltxv] — in: positive:CONDITIONING, negative:CONDITIONING, latent:LATENT | out: positive, negative, latent
- `LTXVDualCFGGuider` [model/sampling/guiders] — in: model:MODEL, positive:CONDITIONING, negative:CONDITIONING, video_cfg:FLOAT, audio_cfg:FLOAT | out: GUIDER
- `LTXVEmptyLatentAudio` [model/latent/ltxv] — in: frames_number:INT, frame_rate:FLOAT,INT, batch_size:INT, audio_vae:VAE | out: Latent
- `LTXVImgToVideoInplace` [model/conditioning/ltxv] — in: vae:VAE, image:IMAGE, latent:LATENT, strength:FLOAT, bypass:BOOLEAN | out: latent
- `LTXVLatentUpsampler` [model/latent/ltxv] — in: samples:LATENT, upscale_model:LATENT_UPSCALE_MODEL, vae:VAE | out: LATENT
- `LTXVSeparateAVLatent` [model/latent/ltxv] — in: av_latent:LATENT | out: video_latent, audio_latent
- `LatentComposite` [model/latent] — in: samples_to:LATENT, samples_from:LATENT, x:INT, y:INT, feather:INT | out: LATENT
- `LatentUpscale` [model/latent] — in: samples:LATENT, upscale_method=«nearest-exact», width:INT, height:INT, crop=«disabled» | out: LATENT
- `LatentUpscaleBy` [model/latent] — in: samples:LATENT, upscale_method=«nearest-exact», scale_by:FLOAT | out: LATENT
- `LatentUpscaleModelLoader` [model/loaders] — in: model_name=«h3_clean_latent_upscaler_film_epoch200.safetensors» | out: LATENT_UPSCALE_MODEL
- `LoraLoader` [model/loaders] — in: model:MODEL, clip:CLIP, lora_name=«Aura_Phantasy_illu.safetensors», strength_model:FLOAT, strength_clip:FLOAT | out: MODEL, CLIP
- `LoraLoaderBypassModelOnly` [model/loaders] — in: model:MODEL, lora_name=«Aura_Phantasy_illu.safetensors», strength_model:FLOAT | out: MODEL
- `LoraLoaderModelOnly` [model/loaders] — in: model:MODEL, lora_name=«Aura_Phantasy_illu.safetensors», strength_model:FLOAT | out: MODEL
- `MMH3LatentUpscaleWithModelParams` [model/latent/minimax] — in: model_name=«h3_clean_latent_upscaler_film_epoch200.safetensors», width:INT, height:INT, device=«cuda», precision=«fp16», offload_model:BOOLEAN | out: latent_upscale_param
- `MMH3UltimateUpscale` [model/latent/minimax] — in: model:MODEL, conditioning:CONDITIONING, latent:LATENT, noise:NOISE, sampler:SAMPLER, sigmas:SIGMAS, cfg:FLOAT | out: latent, segments_info, tiles_info
- `MOSSImageControl` [model/conditioning/moss_image] — in: positive:CONDITIONING, negative:CONDITIONING, vae:VAE, strength:FLOAT, start_percent:FLOAT, end_percent:FLOAT | out: positive, negative
- `MOSSMergePreset` [model/merging/moss] — in: base_model:MODEL, sft_model:MODEL, preset=«Base-preserve», strength:FLOAT, merge_info:STRING, m_video_embedder:FLOAT, m_text_proj:FLOAT, m_text_block0:FLOAT, m_text_block1:FLOAT, m_time:FLOAT, m_shared:FLOAT, m_L00:FL… | out: MODEL
- `ManualSigmas` [model/sampling/sigmas] — in: sigmas:STRING | out: SIGMAS
- `MiniMaxH3AddGuide` [model/conditioning/minimax] — in: positive:CONDITIONING, latent:LATENT, frame_idx:INT | out: positive
- `MiniMaxH3ImageToVideo` [model/conditioning/minimax] — in: clip:CLIP, vae:VAE, prompt:STRING, width:INT, height:INT, length:INT | out: positive, LATENT
- `MiniMaxH3ReferenceToVideo` [model/conditioning/minimax] — in: clip:CLIP, prompt:STRING, width:INT, height:INT, length:INT, ref_image_size=«match» | out: positive, LATENT
- `MiniMaxH3SigmaShift` [model/patch/minimax] — in: model:MODEL, shift_video:FLOAT, shift_audio:FLOAT | out: MODEL
- `MiniMaxMusic3TextEncode` [model/conditioning/minimax music] — in: clip:CLIP, caption:STRING, lyrics:STRING, seed:INT, max_duration:FLOAT, cfg_scale:FLOAT, top_k:INT | out: CONDITIONING, seconds
- `ModelAttentionBackend` [model/patch] — in: model:MODEL, attention=«pytorch attention» | out: model
- `ModelPatchLoader` [model/loaders] — in: name=«Wan2_1-InfiniTetalk-Single_fp16.safetensors» | out: MODEL_PATCH
- `ModelSamplingAuraFlow` [model/patch] — in: model:MODEL, shift:FLOAT | out: MODEL
- `ModelSamplingFlux` [model/patch/flux] — in: model:MODEL, max_shift:FLOAT, base_shift:FLOAT, width:INT, height:INT | out: MODEL
- `ModelSamplingSD3` [model/patch/stable diffusion] — in: model:MODEL, shift:FLOAT | out: MODEL
- `PH3ImageConditioning` [model/conditioning/minimax] — in: clip:CLIP, prompt:STRING, width:INT, height:INT | out: positive, LATENT
- `QwenImage21Cache` [model/conditioning/qwen image] — in: model:MODEL, device=«auto», dtype=«default» | out: MODEL
- `QwenImageDiffsynthControlnet` [model/patch/qwen] — in: model:MODEL, model_patch:MODEL_PATCH, vae:VAE, image:IMAGE, strength:FLOAT | out: MODEL
- `RandomNoise` [model/sampling/noise] — in: noise_seed:INT | out: NOISE
- `ReferenceLatent` [model/conditioning] — in: conditioning:CONDITIONING | out: CONDITIONING
- `RelayVSRConditioning` [model/conditioning/wan] — in: model:MODEL, images:IMAGE | out: positive, latent
- `SamplerCustom` [model/sampling/custom] — in: model:MODEL, add_noise:BOOLEAN, noise_seed:INT, cfg:FLOAT, positive:CONDITIONING, negative:CONDITIONING, sampler:SAMPLER, sigmas:SIGMAS, latent_image:LATENT | out: output, denoised_output
- `SamplerCustomAdvanced` [model/sampling/custom] — in: noise:NOISE, guider:GUIDER, sampler:SAMPLER, sigmas:SIGMAS, latent_image:LATENT | out: output, denoised_output
- `SamplerEulerAncestral` [model/sampling/samplers] — in: eta:FLOAT, s_noise:FLOAT | out: SAMPLER
- `SetLatentNoiseMask` [model/latent] — in: samples:LATENT, mask:MASK | out: LATENT
- `SetUnionControlNetType` [model/conditioning/controlnet] — in: control_net:CONTROL_NET, type=«auto» | out: CONTROL_NET
- `SheetSage2AudioToABC` [model/conditioning/yue2] — in: audio_encoder:AUDIO_ENCODER, audio:AUDIO, mode=«melody» | out: abc
- `SplitSigmas` [model/sampling/sigmas] — in: sigmas:SIGMAS, step:INT | out: high_sigmas, low_sigmas
- `TaoMateHDProgressiveSampler` [model/sampling/taomate] — in: model:MODEL, positive:CONDITIONING, seed:INT, steps:INT, cfg:FLOAT, low_scale:FLOAT, debug:BOOLEAN | out: latent
- `TextEncodeAceStepAudio1.5` [model/conditioning/ace] — in: clip:CLIP, tags:STRING, lyrics:STRING, seed:INT, bpm:INT, duration:FLOAT, timesignature=«2», language=«en», keyscale=«C major», generate_audio_codes:BOOLEAN, cfg_scale:FLOAT, temperature:FLOAT, top_p:FLOAT, top_k:INT,… | out: CONDITIONING
- `TextEncodeQwenImage21` [model/conditioning/qwen image] — in: clip:CLIP, prompt:STRING, negative_prompt:STRING, resolution:INT, images:COMFY_AUTOGROW_V3 | out: positive, negative, latent
- `TextEncodeQwenImageEdit` [model/conditioning/qwen image] — in: clip:CLIP, prompt:STRING | out: CONDITIONING
- `TextEncodeQwenImageEditPlus` [model/conditioning/qwen image] — in: clip:CLIP, prompt:STRING | out: CONDITIONING
- `UNETLoader` [model/loaders] — in: unet_name=«Chroma1/Chroma1-HD-fp8_scaled_rev2.safetensors», weight_dtype=«default» | out: MODEL
- `UniBlockSwap` [model/loaders] — in: model:MODEL | out: model
- `UniBlockSwapTE` [model/loaders] — in: clip:CLIP | out: clip
- `UpscaleModelLoader` [model/loaders] — in: model_name=«1x-ITF-SkinDiffDetail-Lite-v1.pth» | out: UPSCALE_MODEL
- `VAEDecode` [model/latent] — in: samples:LATENT, vae:VAE | out: IMAGE
- `VAEDecodeAudio` [model/latent] — in: samples:LATENT, vae:VAE | out: AUDIO
- `VAEDecodeAudioTiled` [model/latent] — in: samples:LATENT, vae:VAE, tile_size:INT, overlap:INT | out: AUDIO
- `VAEDecodeTiled` [model/latent] — in: samples:LATENT, vae:VAE, tile_size:INT, overlap:INT, temporal_size:INT, temporal_overlap:INT | out: IMAGE
- `VAEEncode` [model/latent] — in: pixels:IMAGE, vae:VAE | out: LATENT
- `VAEEncodeForInpaint` [model/latent] — in: pixels:IMAGE, vae:VAE, mask:MASK, grow_mask_by:INT | out: LATENT
- `VAELoader` [model/loaders] — in: vae_name=«Krea2-HD-vae.safetensors» | out: VAE
- `WanFirstLastFrameToVideo` [model/conditioning/wan] — in: positive:CONDITIONING, negative:CONDITIONING, vae:VAE, width:INT, height:INT, length:INT, batch_size:INT | out: positive, negative, latent
- `WanImageToVideo` [model/conditioning/wan] — in: positive:CONDITIONING, negative:CONDITIONING, vae:VAE, width:INT, height:INT, length:INT, batch_size:INT | out: positive, negative, latent
- `WanInfiniteTalkToVideo` [model/conditioning/wan/infinite talk] — in: mode:COMFY_DYNAMICCOMBO_V3, model:MODEL, model_patch:MODEL_PATCH, positive:CONDITIONING, negative:CONDITIONING, vae:VAE, width:INT, height:INT, length:INT, audio_encoder_output_1:AUDIO_ENCODER_OUTPUT, motion_frame_cou… | out: model, positive, negative, latent, trim_image
- `YuE2GenerateABC` [model/conditioning/yue2] — in: clip:CLIP, style:STRING, lyrics:STRING, seed:INT, mode=«full», max_abc_tokens:INT, temperature:FLOAT, top_p:FLOAT, top_k:INT, repetition_penalty:FLOAT, penalty_window:INT | out: abc
- `YuE2GenerateMusic` [model/conditioning/yue2] — in: clip:CLIP, style:STRING, lyrics:STRING, abc:STRING, seed:INT, mode=«full», max_duration:FLOAT, temperature:FLOAT, top_p:FLOAT, top_k:INT, repetition_penalty:FLOAT | out: CONDITIONING, seconds

## mtb
- `Audio Duration (mtb)` [mtb/audio] — in: audio:AUDIO | out: duration_ms
- `Pick From Batch (mtb)` [mtb/image utils] — in: image:IMAGE, from_direction=«start», count:INT | out: IMAGE, MASK

## rgthree
- `Any Switch (rgthree)` [rgthree] — in: - | out: *
- `Image Comparer (rgthree)` [rgthree] — in: - | out: images
- `Lora Loader Stack (rgthree)` [rgthree] — in: model:MODEL, clip:CLIP, lora_01=«None», strength_01:FLOAT, lora_02=«None», strength_02:FLOAT, lora_03=«None», strength_03:FLOAT, lora_04=«None», strength_04:FLOAT | out: MODEL, CLIP
- `Power Lora Loader (rgthree)` [rgthree] — in: - | out: MODEL, CLIP
- `Seed (rgthree)` [rgthree] — in: seed:INT | out: SEED

## selflift
- `SelfLiftH3Sampler` [selflift] — in: model:MODEL, positive:CONDITIONING, negative:CONDITIONING, vae:VAE, latent_image:LATENT, sampler:SAMPLER, sigmas:SIGMAS, seed:INT, cfg:FLOAT, transition_step:INT, lowres_scale:FLOAT, rho:FLOAT, w_min:FLOAT, w_max:FLOA… | out: LATENT

## selflift-Avatar
- `SelfLiftAvatarH3Sampler` [selflift-Avatar] — in: low_res_model:MODEL, positive:CONDITIONING, negative:CONDITIONING, vae:VAE, latent_image:LATENT, sampler:SAMPLER, sigmas:SIGMAS, seed:INT, cfg:FLOAT, transition_step:INT, lowres_scale:FLOAT, rho:FLOAT, w_min:FLOAT, w_… | out: LATENT

## sol_attn
- `SolAttnMiniMax` [sol_attn] — in: model:MODEL, tau:FLOAT, start_percent:FLOAT, end_percent:FLOAT, min_tokens:INT, sink_conditioning=«exact_kv_and_rows», morton:BOOLEAN, morton_curve=«2d_frame», centroid_tail:BOOLEAN, routed_cap_percent:INT, reuse_qkv_… | out: MODEL

## text
- `StringConcatenate` [text] — in: string_a:STRING, string_b:STRING, delimiter:STRING | out: STRING
- `StringFormat` [text] — in: values:COMFY_AUTOGROW_V3, f_string:STRING | out: STRING
- `StringReplace` [text] — in: string:STRING, find:STRING, replace:STRING | out: STRING
- `TextGenerate` [text] — in: clip:CLIP, prompt:STRING, max_length:INT, sampling_mode:COMFY_DYNAMICCOMBO_V3 | out: generated_text, thinking
- `TextGenerateLTX2Prompt` [text] — in: clip:CLIP, prompt:STRING, max_length:INT, sampling_mode:COMFY_DYNAMICCOMBO_V3 | out: generated_text, thinking

## uncategorized
- `wanBlockSwap` [] — in: model:MODEL | out: MODEL

## utilities
- `ComfyMathExpression` [utilities] — in: expression:STRING, values:COMFY_AUTOGROW_V3 | out: FLOAT, INT, BOOL
- `ComfyNumberConvert` [utilities] — in: value:INT,FLOAT,STRING,BOOLEAN | out: FLOAT, INT
- `ComfySwitchNode` [utilities/logic] — in: switch:BOOLEAN | out: output
- `PreviewAny` [utilities] — in: source:* | out: STRING
- `PrimitiveBoolean` [utilities/primitive] — in: value:BOOLEAN | out: BOOLEAN
- `PrimitiveFloat` [utilities/primitive] — in: value:FLOAT | out: FLOAT
- `PrimitiveInt` [utilities/primitive] — in: value:INT | out: INT
- `PrimitiveString` [utilities/primitive] — in: value:STRING | out: STRING
- `PrimitiveStringMultiline` [utilities/primitive] — in: value:STRING | out: STRING
- `ResolutionSelector` [utilities] — in: aspect_ratio=«1:1 (Square)», megapixels:FLOAT, multiple:INT | out: width, height
- `SeedNode` [utilities] — in: seed:INT | out: seed

## utils
- `MathExpression|pysssss` [utils] — in: expression:STRING | out: INT, FLOAT
- `PlaySound|pysssss` [utils] — in: any:*, mode=«always», volume:FLOAT, file:STRING | out: *
- `ShowText|pysssss` [utils] — in: text:STRING | out: STRING
- `StringFunction|pysssss` [utils] — in: action=«append», tidy_tags=«yes» | out: STRING
- `TTResolutionSelector` [utils] — in: use_custom_resolution:BOOLEAN, resolution=«1024x1024 (1:1) (方形)», custom_width:INT, custom_height:INT | out: width, height
- `mxSlider2D` [utils/mxToolkit] — in: Xi:INT, Xf:FLOAT, Yi:INT, Yf:FLOAT, isfloatX:INT, isfloatY:INT | out: X, Y

## video
- `CreateVideo` [video] — in: images:IMAGE, fps:FLOAT | out: VIDEO
- `FastFilmGrain` [video/enhancement] — in: images:IMAGE, grain_intensity:FLOAT, saturation_mix:FLOAT, batch_size:INT | out: IMAGE
- `GetVideoComponents` [video] — in: video:VIDEO | out: images, audio, fps, bit_depth, color_space
- `LTXVPreprocess` [video/preprocessors] — in: image:IMAGE, img_compression:INT | out: output_image
- `LoadVideo` [video] — in: file=«1741106068055975465.mp4» | out: VIDEO
- `MinimaxH3LatentUpscaler3D` [video/MinimaxH3] — in: latent:*, model_name=«h3_clean_latent_upscaler_film_epoch200.safetensors», mode:COMFY_DYNAMICCOMBO_V3, align:INT, enable_temporal_chunking:BOOLEAN, force_unload:BOOLEAN, device=«cuda», precision=«fp16» | out: latent
- `SaveVideo` [video] — in: video:VIDEO, filename_prefix:STRING, format:COMFY_DYNAMICCOMBO_V3 | out: video

## whisper
- `Apply Whisper` [whisper] — in: audio:AUDIO, model=«tiny.en» | out: text, segments_alignment, words_alignment

## zealman
- `ZealmanH3Dials` [zealman/H3] — in: model:MODEL, enabled:BOOLEAN | out: model, report

## ✨Prompt Assistant
- `ImageCaptionNode` [✨Prompt Assistant] — in: image:IMAGE, rule=«像素级描述（by:阿丹）», custom_rule:BOOLEAN, custom_rule_content:STRING, user_prompt:STRING, vlm_service=«Autodl/gpt-5.5», ollama_auto_unload:BOOLEAN, seed:INT | out: caption_text, caption_list
- `PromptExpand` [✨Prompt Assistant] — in: rule=«扩写-通用», custom_rule:BOOLEAN, custom_rule_content:STRING, user_prompt:STRING, llm_service=«Autodl/gpt-5.5», ollama_auto_unload:BOOLEAN, seed:INT | out: enhanced_text

## 孤海工具箱
- `GuHaiAutoImageSplit` [孤海工具箱] — in: 图像:IMAGE, 保存目录:STRING, 水平张数:INT, 垂直张数:INT, 移除画布边缘:BOOLEAN, 移除描边:INT, 文件名前缀:STRING, 保存格式=«PNG» | out: 分割图像
- `忽略多组孤海` [孤海工具箱] — in: - | out: -

## 🍎MYAPI
- `AutodlApiNode` [🍎MYAPI] — in: api_key:STRING, use_node_api_key:BOOLEAN, model=«qwen3.6-plus», system_prompt:STRING, user_prompt:STRING, seed:INT | out: string
- `DeepSeekV4Node` [🍎MYAPI] — in: api_key:STRING, model=«deepseek-v4-pro», prompt:STRING, enable_thinking:BOOLEAN, reasoning_effort=«高（high）» | out: string, reasoning
- `DoubaoNode` [🍎MYAPI] — in: api_key:STRING, use_node_api_key:BOOLEAN, model=«doubao-seed-2-1-pro-260628», prompt:STRING, max_tokens:INT, seed:INT, reasoning_effort=«均衡思考（medium）» | out: string
- `DoubaoSeedTranslationNode` [🍎MYAPI] — in: api_key:STRING, use_node_api_key:BOOLEAN, model=«doubao-seed-translation-250915», text:STRING, source_language=«zh», target_language=«en» | out: string
- `DoubaoSeedream5Node` [🍎MYAPI] — in: api_key:STRING, use_node_api_key:BOOLEAN, prompt:STRING, size=«2K», custom_width:INT, custom_height:INT, model=«doubao-seedream-4-5-251128», seed:INT, watermark:BOOLEAN, stream:BOOLEAN, sequential_image_generation=«di… | out: image, string
- `segment_text` [🍎MYAPI] — in: text:STRING, split_keyword:STRING, remove_text:STRING, include_keyword:BOOLEAN | out: string_1, string_2, string_3, string_4, string_5, string_6, string_7, string_8, string_9, string_10, string_11, string_12, string_13, string_14, string_15, string_16, string_17, string_18, string_19, string_20

## 🎈LAOGOU
- `LazySwitch1way` [🎈LAOGOU/Switch] — in: boolean:BOOLEAN, ON_TRUE:*, ON_FALSE:* | out: OUTPUT
- `LazySwitch2way` [🎈LAOGOU/Switch] — in: boolean:BOOLEAN, ON_TRUE:*, on_true:*, ON_FALSE:*, on_false:* | out: OUTPUT, output

## 😺dzNodes
- `LayerColor: AutoAdjustV2` [😺dzNodes/LayerColor] — in: image:IMAGE, strength:INT, brightness:INT, contrast:INT, saturation:INT, red:INT, green:INT, blue:INT, mode=«RGB» | out: image
- `LayerColor: BrightnessContrastV2` [😺dzNodes/LayerColor] — in: image:IMAGE, brightness:FLOAT, contrast:FLOAT, saturation:FLOAT | out: image
- `LayerColor: ColorTemperature` [😺dzNodes/LayerColor] — in: image:IMAGE, temperature:FLOAT | out: image
- `LayerMask: MaskPreview` [😺dzNodes/LayerMask] — in: mask:MASK | out: images
- `LayerUtility: BooleanOperatorV2` [😺dzNodes/LayerUtility/Data] — in: a_value:STRING, b_value:STRING, operator=«==» | out: output, string
- `LayerUtility: ColorImage` [😺dzNodes/LayerUtility] — in: width:INT, height:INT, color:STRING | out: image
- `LayerUtility: If ` [😺dzNodes/LayerUtility/Data] — in: if_condition:*, when_TRUE:*, when_FALSE:* | out: ?
- `LayerUtility: ImageMaskScaleAs` [😺dzNodes/LayerUtility] — in: scale_as:*, fit=«letterbox», method=«lanczos» | out: image, mask, original_size, widht, height
- `LayerUtility: ImageReel` [😺dzNodes/LayerUtility] — in: image1:IMAGE, image1_text:STRING, image2_text:STRING, image3_text:STRING, image4_text:STRING, reel_height:INT, border:INT | out: reel
- `LayerUtility: ImageReelComposit` [😺dzNodes/LayerUtility] — in: reel_1:Reel, font_file=«Alibaba-PuHuiTi-Heavy.ttf», font_size:INT, border:INT, color_theme=«light» | out: image1
- `LayerUtility: ImageScaleByAspectRatio V2` [😺dzNodes/LayerUtility] — in: aspect_ratio=«original», proportional_width:INT, proportional_height:INT, fit=«letterbox», method=«lanczos», round_to_multiple=«8», scale_to_side=«None», scale_to_length:INT, background_color:STRING | out: image, mask, original_size, width, height
- `LayerUtility: ImageScaleRestore V2` [😺dzNodes/LayerUtility] — in: image:IMAGE, scale:FLOAT, method=«lanczos», scale_by=«by_scale», scale_by_length:INT | out: image, mask, original_size, width, height
- `LayerUtility: NumberCalculatorV2` [😺dzNodes/LayerUtility/Data] — in: a_value:STRING, b_value:STRING, operator=«+» | out: int, float, string
- `LayerUtility: PurgeVRAM` [😺dzNodes/LayerUtility/SystemIO] — in: anything:*, purge_cache:BOOLEAN, purge_models:BOOLEAN | out: -
- `LayerUtility: PurgeVRAM V2` [😺dzNodes/LayerUtility/SystemIO] — in: anything:*, purge_cache:BOOLEAN, purge_models:BOOLEAN | out: any

## 🧩 Comfyroll Studio
- `CR Float To Integer` [🧩 Comfyroll Studio/🛠️ Utils/🔧 Conversion] — in: _float:FLOAT | out: INT, show_help
- `CR Image Grid Panel` [🧩 Comfyroll Studio/👾 Graphics/🌁 Layout] — in: images:IMAGE, border_thickness:INT, border_color=«custom», outline_thickness:INT, outline_color=«white», max_columns:INT | out: image, show_help
- `CR Prompt Text` [🧩 Comfyroll Studio/✨ Essential/📦 Core] — in: prompt:STRING | out: prompt, show_help
- `CR SDXL Aspect Ratio` [🧩 Comfyroll Studio/✨ Essential/🔳 Aspect Ratio] — in: width:INT, height:INT, aspect_ratio=«custom», swap_dimensions=«Off», upscale_factor:FLOAT, batch_size:INT | out: width, height, upscale_factor, batch_size, empty_latent, show_help
- `CR Seed` [🧩 Comfyroll Studio/✨ Essential/📦 Core] — in: seed:INT | out: seed, show_help
- `CR Text` [🧩 Comfyroll Studio/🛠️ Utils/🔤 Text] — in: text:STRING | out: text, show_help
- `CR Text Concatenate` [🧩 Comfyroll Studio/🛠️ Utils/🔤 Text] — in: - | out: STRING, show_help
- `CR Text Input Switch (4 way)` [🧩 Comfyroll Studio/🛠️ Utils/🔀 Logic] — in: Input:INT | out: STRING, show_help
- `CR Text Replace` [🧩 Comfyroll Studio/🛠️ Utils/🔤 Text] — in: text:STRING | out: STRING, show_help

## 🧪AILab
- `H3_Promptor` [🧪AILab/🎬 MiniMax H3-Promptor] — in: task_type=«Auto», scene_direction:STRING, duration:FLOAT | out: PROMPT, DURATION, LENGTH
- `H3_Vision` [🧪AILab/🎬 MiniMax H3-Promptor] — in: global_image_mode=«Subject / Identity», global_video_mode=«Comprehensive», _media_state:STRING | out: VISION_CONTEXT, REF_IMAGES
