# Contributing

Thanks for helping improve ComfyUI Workflow Builder!

## 快速流程

1. Fork 本仓库并新建分支：`feat/xxx` / `fix/xxx` / `docs/xxx`
2. 本地跑自检：`python scripts/check_repo.py`
3. 提交 PR，说明：改了什么、为什么、在你机器上的验证结果（ComfyUI 版本 / 模型 / 输出）

## 新增 recipe 模板

- 放 `templates/<family>-<task>.json`，遵循 `SKILL.md` 的 recipe DSL；
- 在 `templates/README.md` 的表格里加一行（用途 + 结构校验状态 + 是否实跑过）；
- 模型名请用**你机器 `/object_info` 里的真实文件名**，并在 PR 里注明版本；
- 如果只做了离线校验，请在表格里写"⏳ 未实跑"，不要声称实跑通过。

## 修改文档

- `references/` 下的实例相关描述请保持"参考实例"措辞，不要把个人机器信息（host/密码/路径）写进去；
- 更新 `CHANGELOG.md`。

## 安全

- 不要提交 `instance.json`、`.cache/`、生成产物或任何 token；
- 发现安全问题请走 [SECURITY.md](SECURITY.md)，不要开公开 issue。
