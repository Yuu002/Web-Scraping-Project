import streamlit as st
import pickle
import matplotlib.pyplot as plt

st.title("Product Sale Perdition")

# โหลดผลลัพธ์และโมเดลจากไฟล์ pickle
@st.cache
def load_data():
    with open('results.pkl', 'rb') as file:
        results = pickle.load(file)
    return results

results = load_data()

if results is not None:
    # แสดงตารางผลลัพธ์
    st.subheader("Sales Forecast Results")
    st.write(results)

    # สร้าง selectbox ให้ผู้ใช้เลือกผลิตภัณฑ์
    selected_products = st.multiselect("Select Products:", results['Product_names'].tolist(), default=results['Product_names'].tolist())

    # กรองข้อมูลตามผลิตภัณฑ์ที่เลือก
    filtered_results = results[results['Product_names'].isin(selected_products)]

    # แสดงกราฟแท่งแนวนอน
    st.subheader("Current vs Forecasted Sales")
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.barh(filtered_results['Product_names'], filtered_results['Current_Sold_out'], color='blue', label='Current Sales')
    ax.barh(filtered_results['Product_names'], filtered_results['Forecasted_Sold_out'], color='red', alpha=0.6, label='Forecasted Sales')
    ax.set_xlabel('Sales')
    ax.set_ylabel('Product')
    ax.set_title('Comparison of Current Sales and Forecasted Sales')
    ax.legend()
    ax.grid(axis='x')
    st.pyplot(fig)
else:
    st.write("Please upload the analysis results to proceed.")