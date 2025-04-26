# ⚡ Alive Progress
## Because Your Progress Bars Deserve to Vibe

**alive-progress** is a Python package that gives your terminal progress bars a pulse. Unlike the basic, boring ones, this tool brings animated, customizable, real-time progress bars with a heartbeat — **no lag, no limits, pure style**.

---

## 🎯 What It Does

- 🎞️ **Smooth Animations**: Real-time frame-by-frame animations that feel alive (hence the name).
- 🌈 **Custom Themes**: Pick from a variety of spinner styles, bar shapes, and color combos.
- 🧮 **Smart Handling**: Automatically adapts to terminal size, supports dynamic resizing, and handles keyboard interrupts like a champ.
- ⚖️ **Concurrent Compatibility**: Works great with threads and multiprocessing without weird side effects.
- 🧠 **Auto ETA & Rate**: Calculates time remaining and speed of iteration like a pro.
- 📦 **Nested Bars**: Yup, it can handle multiple progress bars running together.

---

## 📦 Installation

```bash
pip install alive-progress
```

## 🚀 Example
```py
from alive_progress import alive_bar
import time

with alive_bar(100) as bar:
    for _ in range(100):
        time.sleep(0.02)
        bar()
```
Boom — a slick, animated progress bar counting up to 100 with zero setup.

---

## 💡 Why Use It?
Other progress bars work. alive-progress performs. It's all about the experience: fluid animations, intuitive API, and customizable flair. Whether you're crunching data, downloading files, or training models — this bar brings the drip.