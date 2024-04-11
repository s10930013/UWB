document.addEventListener('DOMContentLoaded', function () {
    // 定時檢查圖片更新
    setInterval(updateImage, 5000); // 每5秒檢查一次

    function updateImage() {
        // 使用Ajax或其他方法檢查伺服器上的圖片是否有更新
        // 如果有更新，則更新圖片的src屬性
        // 這只是一個示例，實際上需要根據你的需求實現相應的邏輯
        // 以下為示例，需要根據實際情況修改
        var imgElement = document.getElementById('dynamicImage');
        var imageUrl = "path/to/your/image.jpg";

        var xhr = new XMLHttpRequest();
        xhr.open('HEAD', imageUrl, true);
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
                if (xhr.status === 200) {
                    // 圖片有更新，更新圖片的src屬性
                    imgElement.src = imageUrl + "?timestamp=" + new Date().getTime();
                }
            }
        };
        xhr.send();
    }
});
