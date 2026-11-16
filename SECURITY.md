# Security Policy

## 报告问题

请通过 GitHub 的 **Security → Report a vulnerability**（私有安全通告）报告，不要在公开 issue 里贴 token、密码或主机地址。

## 本仓库的安全约定

- 仓库不含任何凭据；连接信息放在本地 `instance.json`（已 `.gitignore`）或环境变量。
- `scripts/check_repo.py` 会扫描 token/私钥样式字符串，CI 每次 push 都会跑。
- 使用 SSH 密码认证仅用于隧道；更推荐改用 SSH key（可自行修改 `scripts/remote.py` 的 `connect()`）。
- 请只在你拥有或获授权的 ComfyUI 实例上使用本技能；模型与生成内容的许可由使用者负责。
