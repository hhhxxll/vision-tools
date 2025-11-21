# 📸 Vision-Learning (机器视觉实战笔记)

> **项目简介**：
> 这是一个结合 **工业现场经验** 与 **Python 算法** 的实战代码库。
> 旨在将传统的视觉调试经验（如打光、标定、定位）转化为自动化、可复用的 Python 脚本，并探索 YOLO 深度学习在工业缺陷检测中的应用。

---

## 🛠 核心功能 (Features)

### Phase 1: 工程化基础 (进行中)
- [x] **数据预处理工具** (`data_tool.py`): 
    - 支持命令行参数 (`argparse`) 批量处理图片。
    - 集成自动重命名、尺寸缩放 (`resize`)、格式转换功能。
    - 包含完整的日志记录 (`logging`)，摒弃 Print 调试。

### Phase 2: 传统视觉算法 (计划中)
- [ ] **定位与测量**: 复现工业场景下的模板匹配与找圆算法。
- [ ] **标定工具**: 9点标定与畸变矫正算法实现。

### Phase 3: 深度学习落地 (计划中)
- [ ] **缺陷检测**: 基于 YOLOv8 的工业外观缺陷检测系统。

---

## 💻 技术栈 (Tech Stack)
- **Language**: Python 3.8+
- **Libraries**: OpenCV, NumPy, PyTorch, Ultralytics (YOLO)
- **Tools**: PyCharm, Git

---
*Last updated: 2025-11-21*
