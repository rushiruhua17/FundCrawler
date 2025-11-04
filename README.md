# FundCrawler - 基金数据爬取与可视化分析系统

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

一个功能强大的基金数据爬取、分析与可视化系统，支持从多个数据源采集基金信息并进行深度分析。

</div>

## 📋 目录

- [项目简介](#项目简介)
- [主要功能](#主要功能)
- [技术栈](#技术栈)
- [项目结构](#项目结构)
- [快速开始](#快速开始)
- [使用说明](#使用说明)
- [数据说明](#数据说明)
- [可视化展示](#可视化展示)
- [注意事项](#注意事项)
- [贡献指南](#贡献指南)
- [许可证](#许可证)

## 🎯 项目简介

FundCrawler 是一个专业的基金数据采集与分析系统，通过爬取天天基金网、晨星网等权威平台的数据，为投资者提供全面的基金信息分析和可视化展示。

### 核心特性

- 🚀 **高效爬取**：采用多进程架构，支持大规模基金数据并行采集
- 📊 **数据分析**：提供全面的基金风险指标、收益率、夏普比率等核心数据
- 📈 **可视化展示**：基于 ECharts 的交互式数据可视化平台
- 🔄 **智能重试**：内置请求失败重试机制，确保数据完整性
- 📝 **多格式导出**：支持 CSV、JSON、XLSX 等多种数据格式

## ✨ 主要功能

### 1. 数据采集
- 爬取全市场开放式基金基本信息
- 采集基金管理人、基金经理详细数据
- 获取基金费率信息（管理费、托管费、销售服务费）
- 收集基金净值、资产规模等关键指标

### 2. 风险分析
- 标准差分析（五年/十年）
- 夏普比率计算
- 阿尔法系数、贝塔系数
- R平方指标

### 3. 收益分析
- 年化收益率（五年/十年）
- 历史回报率趋势
- 基金类型维度收益对比

### 4. 数据可视化
- 基金总数统计
- 基金类型分布
- 资产规模等级分布
- 管理人基金数量排名
- 夏普比率趋势对比
- 年回报率概览

## 🛠 技术栈

### 后端技术
- **Python 3.8+**
- **Flask**：Web 框架，提供数据 API
- **Requests**：HTTP 请求库
- **Scrapy**：爬虫框架（部分组件）
- **Pandas**：数据处理与分析
- **Threading/Multiprocessing**：多线程/多进程支持

### 前端技术
- **HTML5/CSS3**
- **JavaScript**
- **ECharts 5.x**：数据可视化
- **Axios**：HTTP 客户端

### 数据源
- 天天基金网 (eastmoney.com)
- 晨星网 (morningstar.cn)

## 📁 项目结构

```
FundCrawler/
├── module/                          # 核心模块
│   ├── crawling_target/            # 爬取目标模块
│   │   ├── get_fund_by_web.py     # 从网页获取基金列表
│   │   ├── get_fund_4_retry.py    # 重试失败任务
│   │   ├── get_small_batch_4_test.py  # 小批量测试
│   │   └── get_special_fund.py    # 特定基金爬取
│   ├── data_mining/                # 数据挖掘模块
│   │   ├── data_mining.py         # 数据挖掘主逻辑
│   │   └── strategy/              # 数据挖掘策略
│   │       ├── overview.py        # 基金概况
│   │       ├── manager.py         # 基金经理
│   │       ├── morningstar.py     # 晨星数据
│   │       ├── fund_return.py     # 收益数据
│   │       └── risk.py            # 风险指标
│   ├── downloader/                 # 下载器模块
│   │   ├── download_by_requests.py # 请求下载器
│   │   └── rate_control/          # 访问频率控制
│   ├── saving_result/              # 结果保存模块
│   │   └── save_result_2_file.py  # 保存到文件
│   ├── fund_context.py             # 基金上下文
│   ├── process_manager.py          # 任务管理器
│   └── abstract_*.py               # 抽象基类
├── e-chart/                         # 可视化平台
│   ├── app.py                      # Flask 应用
│   ├── static/
│   │   └── index.html             # 可视化页面
│   └── data/                       # 可视化数据
│       ├── 基金总数.csv
│       ├── 各类型基金总数.csv
│       ├── 资产规模等级分布图.csv
│       └── ...
├── result/                          # 爬取结果
│   ├── result.csv                  # 完整数据
│   ├── separate/                   # 分类数据
│   │   ├── fund_data_info.csv     # 基本信息
│   │   ├── fund_data_manager.csv  # 管理人信息
│   │   ├── fund_data_risks.csv    # 风险指标
│   │   └── fund_data_fees.csv     # 费率信息
│   └── Csv_To_Json&xlsx.py        # 格式转换工具
├── utils/                           # 工具模块
│   ├── constants.py                # 常量定义
│   ├── fake_ua_getter.py          # User-Agent 生成
│   ├── rate_control_analyse.py    # 频率控制分析
│   └── top_k_holder.py            # Top-K 持有人
├── run.py                           # 主程序入口
├── requirements.txt                 # 依赖列表
├── .gitignore                      # Git 忽略配置
└── README.md                        # 项目文档
```

## 🚀 快速开始

### 环境要求

- Python 3.8 或更高版本
- pip 包管理器
- 稳定的网络连接

### 安装步骤

1. **克隆项目**
```bash
git clone https://github.com/yourusername/FundCrawler.git
cd FundCrawler
```

2. **创建虚拟环境**（推荐）
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **安装依赖**
```bash
pip install -r requirements.txt
```

### 运行程序

#### 1. 数据爬取

```bash
python run.py
```

爬取完成后，数据将保存在 `result/result.csv` 文件中。

#### 2. 数据可视化

```bash
cd e-chart
python app.py
```

访问 `http://127.0.0.1:5000/` 查看可视化页面。

## 📖 使用说明

### 爬取策略选择

在 `run.py` 中可以选择不同的爬取策略：

```python
from module.crawling_target.get_fund_by_web import GetFundByWeb  # 爬取全部基金
# from module.crawling_target.get_small_batch_4_test import GetSmallBatch4Test  # 小批量测试
# from module.crawling_target.get_fund_4_retry import GetFund4Retry  # 重试失败任务

TaskManager(GetFundByWeb(), DataMining(), SaveResult2CSV()).run()
```

### 数据处理

#### 分离数据到不同文件

```bash
cd result/separate
python separate_fund_data.py
```

生成的文件包括：
- `fund_data_info.csv` - 基金基本信息
- `fund_data_manager.csv` - 基金经理信息
- `fund_data_risks.csv` - 风险指标
- `fund_data_fees.csv` - 费率信息

#### 格式转换

```bash
cd result
python Csv_To_Json&xlsx.py
```

支持转换为：JSON、XLSX、XML 等格式。

### 自定义配置

#### 修改日志级别

在 `run.py` 中：

```python
logging.basicConfig(level=logging.INFO, format=log_format)  # INFO, DEBUG, WARN, ERROR
```

#### 调整爬取频率

在 `module/downloader/rate_control/rate_control.py` 中调整请求间隔。

## 📊 数据说明

### 主要字段

| 字段名 | 说明 | 示例 |
|--------|------|------|
| 基金代码 | 6位基金代码 | 000001 |
| 基金简称 | 基金名称 | 华夏成长混合 |
| 基金类型 | 基金分类 | 混合型 |
| 资产规模(亿) | 基金规模 | 50.23 |
| 基金管理人 | 管理公司 | 华夏基金 |
| 基金经理 | 经理姓名 | 张三 |
| 五年回报(年化) | 年化收益率 | 15.6% |
| 标准差(五年%) | 风险指标 | 18.5% |
| 夏普比率(五年) | 风险调整收益 | 0.85 |
| 管理费率(每年) | 管理费 | 1.5% |

### 数据特殊标记

- `NO_DATA` - 该字段无数据
- `DATA_ERROR` - 数据获取异常
- `DATA_IGNORE` - 数据被忽略

## 📈 可视化展示

### 主要图表

1. **基金总数统计卡片**
   - 显示系统中基金总数量
   - 基金管理人数量
   - 基金经理总人数

2. **资产规模分析**
   - 总资产规模统计
   - 平均资产规模
   - 资产规模等级分布

3. **基金类型分析**
   - 各类型基金数量
   - 基金类型占比
   - 类型维度收益对比

4. **风险收益分析**
   - 夏普比率趋势
   - 年回报率概览
   - 风险指标对比

5. **管理人排名**
   - Top 6 管理人基金数量
   - 管理规模排名

### 交互功能

- 切片器筛选（基金类型、管理人、经理）
- 图表联动
- 数据详情查看
- 图表缩放、平移

## ⚠️ 注意事项

### 法律与道德

1. **遵守 Robots 协议**：爬取前请检查目标网站的 `robots.txt`
2. **合理使用数据**：仅用于个人学习和研究，不得用于商业用途
3. **尊重版权**：数据版权归原网站所有
4. **访问频率控制**：避免对目标服务器造成压力

### 技术建议

1. **网络环境**：建议在稳定网络环境下运行
2. **运行时间**：全量爬取可能需要数小时
3. **数据更新**：建议定期更新数据以保持时效性
4. **异常处理**：如遇爬取失败，可使用重试模块

### 常见问题

**Q1: 爬取速度慢怎么办？**
A: 可以调整并发数量，但需注意遵守访问频率限制。

**Q2: 部分数据显示 NO_DATA？**
A: 这表明该基金在数据源中确实没有该项数据，属于正常现象。

**Q3: 可视化页面无法显示数据？**
A: 请确保已运行数据爬取，并且 `e-chart/data/` 目录下有相应的 CSV 文件。

**Q4: 如何只爬取特定基金？**
A: 使用 `get_special_fund.py` 模块，修改其中的基金代码列表。

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

### 贡献步骤

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

### 代码规范

- 遵循 PEP 8 编码规范
- 添加必要的注释和文档
- 编写单元测试

## 📝 更新日志

### Version 1.0.0
- ✅ 基础爬虫功能
- ✅ 多进程下载支持
- ✅ 数据可视化平台
- ✅ CSV/JSON/XLSX 导出

## 📄 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

## 👨‍💻 作者

**Your Name**

- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🙏 致谢

- 数据来源：[天天基金网](http://fund.eastmoney.com/)、[晨星网](https://www.morningstar.cn/)
- 可视化：[Apache ECharts](https://echarts.apache.org/)
- Web 框架：[Flask](https://flask.palletsprojects.com/)

## ⭐ Star History

如果这个项目对你有帮助，请给一个 Star ⭐️ 支持一下！

---

<div align="center">
Made with ❤️ by FundCrawler Team
</div>

