// このファイルはQRコードを読み込むためのJavaScriptロジックを実装しています。

const video = document.createElement('video');
const canvasElement = document.createElement('canvas');
const canvas = canvasElement.getContext('2d');
const resultContainer = document.createElement('div');
document.body.appendChild(video);
document.body.appendChild(canvasElement);
document.body.appendChild(resultContainer);

function startCamera() {
    navigator.mediaDevices.getUserMedia({ video: { facingMode: 'environment' } })
        .then(stream => {
            video.srcObject = stream;
            video.setAttribute('playsinline', true);
            video.play();
            requestAnimationFrame(tick);
        })
        .catch(err => {
            console.error("カメラへのアクセスに失敗しました:", err);
        });
}

function tick() {
    if (video.readyState === video.HAVE_ENOUGH_DATA) {
        canvasElement.height = video.videoHeight;
        canvasElement.width = video.videoWidth;
        canvas.drawImage(video, 0, 0, canvasElement.width, canvasElement.height);
        const imageData = canvas.getImageData(0, 0, canvasElement.width, canvasElement.height);
        // QRコードのスキャン処理をここに追加
        // 例: const code = jsQR(imageData.data, imageData.width, imageData.height);
        // if (code) { resultContainer.textContent = code.data; }
    }
    requestAnimationFrame(tick);
}

startCamera();