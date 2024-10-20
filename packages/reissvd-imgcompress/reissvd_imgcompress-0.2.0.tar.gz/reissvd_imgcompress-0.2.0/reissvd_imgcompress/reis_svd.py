import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from scipy.linalg import svd, solve_sylvester
from skimage.metrics import structural_similarity as ssim

#
def rgb2gray(image):
    """將 RGB 圖像轉換為灰階圖像。"""
    return np.dot(image[...,:3], [0.2989, 0.5870, 0.1140])

#
def reis_svd(image_matrix, k, max_iter=50, tol=1e-6):
    """
    使用 REIS-SVD 進行圖像壓縮。
    """
    # Step 1: 初始 SVD 分解
    U, S, Vt = svd(image_matrix, full_matrices=False)

    # 確保 k 不超過奇異值的數量
    if k > len(S):
        k = len(S)

    # 確保 A11 和 A22 為 (k, k) 的方形矩陣
    A11 = U[:k, :k]
    A22 = U[:k, :k]
    R = np.zeros((k, k))  # 初始化 R

    # Step 2: 使用牛頓法解 Sylvester 方程
    for _ in range(max_iter):
        R_new = solve_sylvester(A22, A11, -A22 @ A11)
        if np.linalg.norm(R_new - R) < tol:  # 收斂檢查
            break
        R = R_new

    # Step 3: 使用優化結果重建圖像
    Sigma_k = np.diag(S[:k])
    compressed_image = U[:, :k] @ Sigma_k @ Vt[:k, :]

    return np.clip(compressed_image.astype(float), 0, 255)


#
def compute_metrics(original_image, compressed_image, k):
    """
    計算 CR、MSE、PSNR、SSIM。
    
    參數:
    original_image: 原始的灰階圖像。
    compressed_image: 壓縮後的灰階圖像。
    k: 保留的奇異值數量。
    
    返回:
    CR: 壓縮比率。
    mse: 均方誤差。
    psnr: 峰值信噪比。
    ssim_index: 結構相似性指數。
    """
    # 計算 CR (Compression Ratio)
    original_size = original_image.size  # 原始圖像的像素數量
    compressed_size = k * (compressed_image.shape[0] + compressed_image.shape[1] + 1)  # U 的列數 + S + V 的列數
    CR = original_size / compressed_size
    
    # 計算 MSE (Mean Squared Error)
    mse = np.mean((original_image - compressed_image) ** 2)
    
    # 計算 PSNR (dB)
    max_pixel_value = 255.0
    psnr = 10 * np.log10((max_pixel_value ** 2) / mse)
    
    # 計算 SSIM
    ssim_index = ssim(original_image, compressed_image, data_range=max_pixel_value)
    
    return CR, mse, psnr, ssim_index


#
def plot_compressed_images(gray_image, k_values):
    """
    同時顯示不同 k 值下壓縮的圖像，每行最多 3 張圖。
    
    參數:
    gray_image: 灰階圖像矩陣。
    k_values: 奇異值的取值列表。
    """
    n = len(k_values)
    rows = (n // 3) + (1 if n % 3 != 0 else 0)  # 計算需要的行數，每行最多 3 張圖

    fig, axes = plt.subplots(rows, 3, figsize=(15, 5 * rows))
    axes = axes.flatten()  # 將 axes 陣列攤平，方便迭代

    for i, k in enumerate(k_values):
        compressed_image = reis_svd(gray_image, k)
        axes[i].imshow(compressed_image, cmap='gray')
        axes[i].set_title(f'k={k}')
        axes[i].axis('off')

    # 將多餘的子圖隱藏
    for j in range(len(k_values), len(axes)):
        axes[j].axis('off')

    plt.tight_layout()
    plt.show()
