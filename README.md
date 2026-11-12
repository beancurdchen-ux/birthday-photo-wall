# 3D 生日蛋糕 & 照片墙

一个纯前端的 3D 生日祝福页面：Three.js 线框蛋糕 + 旋转照片球，支持鼠标、按钮和摄像头手势三种交互方式，附带全屏烟花动画。

照片和文案都是示例内容，替换成你自己的照片即可使用。

## 功能

- 3D 线框蛋糕，蜡烛火焰有轻微跳动
- 照片球：照片按原始宽高比显示，不会被拉伸；可上下左右旋转，无操作时自动慢速旋转
- 点击照片查看详情：放大显示 + 文字说明
- 手势控制（摄像头）：
  - ✋ 张开手掌 → 切换到照片墙
  - 👌 捏合 → 查看画面中央那张照片的详情
  - ✌️ 比耶 → 放全屏烟花
- 全屏烟花：多种形态、随机颜色
- 渲染库全部放在本地 `lib/` 目录，不依赖 CDN

## 快速开始

**必须通过本地服务器打开**。直接双击 `index.html` 会触发浏览器的跨域限制，照片加载不出来。

Windows：双击 `启动.bat`（需要已安装 Python 3，会自动打开浏览器）。

其它系统或手动启动：

```bash
python -m http.server 8000
```

然后访问 <http://localhost:8000>。

推荐使用 Chrome / Edge。

## 换成自己的照片和文案

1. 把照片命名为 `1.jpg`、`2.jpg`……连续编号，放进 `images/` 目录（建议先把宽度压到 1200px 左右，太大加载慢）
2. 打开 `index.html`，找到 `const TOTAL_PHOTOS = 12;`，改成你的照片张数
3. 照片较多时，把 `PHOTO_RADIUS` 调大一些，避免照片互相拥挤：
   - 12 张 → 20
   - 40 张 → 25
4. 文案写在 `captions.js` 里，键名就是照片序号：

```js
window.PHOTO_CAPTIONS = {
    1: { title: "2024年3月16日 20:15", desc: "这里写这张照片的故事" }
};
```

没有写文案的照片，点击后只会放大显示，不出现文字。

5. `images/` 里现在是 12 张 AI 生成的示例图，可以全部删除后换成自己的照片。

## 关于手势

- 需要摄像头权限，且页面必须通过 `localhost` 或 `https` 打开
- 手势识别使用 MediaPipe Hands，从 unpkg CDN 加载，首次打开需要联网
- 如果网络访问不了 unpkg，页面会提示“手势库加载失败(可用按钮)”，此时用按钮和鼠标操作一切正常
- 捏合手势要求连续多帧成立且手基本静止，避免转动照片墙时误触发

## 目录结构

```
index.html    页面结构与 3D 场景、交互逻辑
captions.js   照片文案（与照片序号对应）
images/       照片，1.jpg ~ N.jpg
lib/          three.js / OrbitControls / GSAP 本地库
server.py     本地静态服务器
启动.bat      Windows 一键启动脚本
```

## 技术栈

| 库 | 版本 | 用途 |
| --- | --- | --- |
| [Three.js](https://threejs.org/) | r128 | 3D 场景、模型、纹理 |
| OrbitControls | r128 | 鼠标旋转 / 缩放视角 |
| [GSAP](https://gsap.com/) | 3.12.2 | 状态切换动画 |
| [MediaPipe Hands](https://developers.google.com/mediapipe) | CDN 最新版 | 摄像头手势识别 |

## 第三方库许可

- Three.js、OrbitControls：MIT
- GSAP：GreenSock Standard License（个人与商业项目均可免费使用，详见 <https://gsap.com/standard-license/>）
- MediaPipe Hands：Apache License 2.0
- `images/` 中的示例图片由 AI 生成，仅作占位使用

## License

本项目自己的代码使用 MIT License，详见 [LICENSE](LICENSE)。
