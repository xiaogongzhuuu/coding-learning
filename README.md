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
- **前端**：Node.js（仅在需要前端开发时）

## 安装依赖
### 后端依赖
在项目根目录下运行以下命令安装后端依赖：
```bash
pip install -r requirements.txt
```

### 前端依赖
如果需要前端开发，请在 `frontend` 目录下运行以下命令安装依赖：
```bash
npm install
```
> 如果 `frontend` 目录中没有 `package.json` 文件，可以跳过此步骤。

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
│   ├── learning.py  # 学习相关模块
│   ├── main.py      # 后端入口文件
│   ├── transformers.py # AI 模型处理模块
├── frontend/        # 前端代码
│   ├── index.html   # 前端页面入口
│   ├── main.js      # 前端主逻辑
│   ├── style.css    # 前端样式文件
├── README.md        # 项目说明文件
├── requirements.txt # Python 依赖文件
├── longchain.ipynb  # Jupyter Notebook 示例
└── .gitignore       # Git 忽略文件
```

## 注意事项
- 确保在运行后端服务前已安装所有依赖。
- 前端页面仅为静态展示，未集成动态功能。
- 请勿将敏感信息（如 API 密钥）暴露在代码中。

## 作者
- xiaogongzhuuu
