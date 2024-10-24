import streamlit as st
import numpy as np

st.title("重力加速度計算アプリ")

## 入力セクション
st.header("入力")
height = st.number_input("落下高さ (メートル)", min_value=0.1, value=10.0, step=0.1)
time = st.number_input("落下時間 (秒)", min_value=0.1, value=2.0, step=0.1)

## 計算セクション
def calculate_gravity(h, t):
    return (2 * h) / (t ** 2)

if st.button("計算"):
    gravity = calculate_gravity(height, time)
    
    ## 結果表示セクション
    st.header("結果")
    st.write(f"計算された重力加速度: {gravity:.2f} m/s²")
    
    ## 理論値との比較
    theoretical_gravity = 9.81
    error = abs(gravity - theoretical_gravity) / theoretical_gravity * 100
    
    st.write(f"理論値との誤差: {error:.2f}%")
    
    ## 視覚化セクション
    st.header("落下の視覚化")
    t = np.linspace(0, time, 100)
    h = height - 0.5 * theoretical_gravity * t**2
    
    st.line_chart({"高さ (m)": h}, use_container_width=True)

## 注意事項
st.info("注: この計算は空気抵抗を無視した理想的な状況を想定しています。")