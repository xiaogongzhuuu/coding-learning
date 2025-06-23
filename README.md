# 学习项目（Learning Project）

## 项目简介
这是一个用于学习和实验的项目，包含前端和后端两部分。后端基于Python，前端为简单的网页应用。

## 环境要求
- Python 3.8 及以上
- Node.js（如需前端开发）

## 依赖安装
### 后端依赖
在项目根目录下运行：
```bash
pip install -r requirement.txt
```

### 前端依赖
如有前端依赖，请在 `frontend` 目录下运行：
```bash
npm install
```
（如无 package.json 可忽略此步）

## 运行方法
### 启动后端
```bash
python backend/main.py
```

### 启动前端
直接用浏览器打开 `frontend/index.html` 即可。

## 目录结构
```
vscode/
  backend/         # 后端代码
    learning.py    # 学习相关模块
    main.py        # 后端入口
  frontend/        # 前端代码
    index.html     # 前端页面入口
    main.js        # 前端主逻辑
  README.md        # 项目说明
  requirement.txt  # Python依赖
```

## 主要功能
- 后端：提供AI相关的接口与逻辑处理
- 前端：展示和交互界面

## 作者
- 你的名字
