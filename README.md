# car-park-detection-v1
**File Hierarchy**

```
CAR-PARK-DETECTION-V1/
├── output/
│   └── carPark_pos.pickle
├── src/
│   ├── carPark.mp4
│   └── carPark.png
├── utils/
│   ├── frame_from_video.py
│   └── select_parking_spaces.py
├── venv/
├── .gitignore
├── main.py
├── README.md
└── requirements.txt

```

---

# Car Park Detection V1

**A simple, fixed-camera car-park space detector & counter using OpenCV.**

## 🚀 Quick Start

1. **Clone & install**
    
    ```bash
    git clone <repo-url>
    cd car-park-detection-v1
    pip install -r requirements.txt
    
    ```
    
2. **Define ROIs**
    
    ```bash
    python utils/select_parking_spaces.py
    
    ```
    
    - Click to mark each space, then ✓ to save `output/carPark_pos.pickle`.
3. **Run the detector**
    
    ```bash
    python main.py
    
    ```
    
    - Streams `src/carPark.mp4`, draws colour-coded boxes, and shows free/total count.

## 📂 What’s Inside

- **output/** – saved ROI coordinates
- **src/** – sample video & reference image
- **utils/**
    - `frame_from_video.py` – extract stills if needed
    - `select_parking_spaces.py` – GUI for marking spaces
- **main.py** – full detection pipeline
- **requirements.txt** – dependencies

---

### 📚 Author & Portfolio

**Emere Ejor**
AI/ML Engineer & Full-Stack Developer
[Portfolio](https://ai-ml-portfolio-h7hv.vercel.app/) • [GitHub](https://github.com/emereshub)

Feel free to connect or raise issues/suggestions!

Feel free to connect or raise issues/suggestions!
