# 学习项目（Learning Project）

## 项目简介

这是一个用于学习和实验的项目，包含后端和前端两部分。后端基于 Python，前端为简单的网页应用。项目旨在探索 AI 技术、数据处理以及前端交互设计。

## 项目目标

本项目旨在探索以下领域：

- 使用 AI 技术进行数据处理和分析。
- 构建简单的前端交互界面。
- 学习后端 API 的设计与实现。

## 环境要求

- **后端**：Python 3.8 或更高版本
- **前端**：现代浏览器（支持 HTML/CSS/JS）

## 安装依赖

### 后端依赖

在项目根目录下运行以下命令安装后端依赖：

```bash
pip install -r requirements.txt
```

### 前端依赖

前端为静态页面，无需额外安装依赖。

## 运行项目

### 启动后端

运行以下命令启动后端服务：

```bash
python backend/main.py
```

后端提供以下 API 路由：

- `/hello?name=名字`：返回问候语。
- `/multiply?n1=数字1&n2=数字2`：返回两个数字的乘积。
- `/user/{name}`：返回用户的问候语。
- `/square/{number}`：返回数字的平方。

### 启动前端

直接使用浏览器打开 `frontend/index.html` 文件即可查看前端页面。

## 项目目录结构

```
vscode/
├── backend/         # 后端代码
│   ├── main.py      # 后端入口文件
│   ├── transformers.py # AI 模型处理模块
├── frontend/        # 前端代码
│   ├── index.html   # 前端页面入口
│   ├── page.html    # 前端子页面
│   ├── main.js      # 前端主逻辑
│   ├── style.css    # 前端样式文件
├── README.md        # 项目说明文件
├── requirements.txt # Python 依赖文件
├── LICENSE          # 开源许可证文件
├── .gitignore       # Git 忽略文件
└── .env             # 环境变量文件
```

## 注意事项

- 确保在运行后端服务前已安装所有依赖。
- 前端页面仅为静态展示，未集成动态功能。
- 请勿将敏感信息（如 API 密钥）暴露在代码中。

## 示例

### 后端 API 示例

1. 访问 `http://127.0.0.1:8000/hello?name=张三`，返回问候语。
2. 访问 `http://127.0.0.1:8000/multiply?n1=3&n2=5`，返回乘积结果。
3. 访问 `http://127.0.0.1:8000/square?number=10`，返回平方结果。

### 前端页面示例

1. 打开 `frontend/index.html`，输入数字并点击按钮查看计算结果。
2. 点击链接跳转到子页面 `page.html`。

## 作者

- xiaogongzhuuu

## 开源许可证

本项目使用 [MIT License](LICENSE) 进行授权。
