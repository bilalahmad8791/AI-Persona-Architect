import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from io import BytesIO

# --- Page Configuration ---
st.set_page_config(layout="wide", page_title="AI Persona Architect")

# --- Main Title ---
st.title("🤖 AI Persona Architect")
st.write("---")

# --- Sidebar for Controls ---
with st.sidebar:
    st.header("1. Upload Your Data")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    data = None  # Initialize data to None
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
    
    if data is not None:
        st.write("---")
        st.header("2. Configure Personas")
        
        # Select features for clustering
        numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns.tolist()
        # A more relevant default selection for the mall dataset
        default_features = ['Age', 'Annual Income (k$)', 'Spending Score (1-100)']
        
        features_for_clustering = st.multiselect(
            "Select features for persona creation:",
            numeric_columns,
            default=[feat for feat in default_features if feat in numeric_columns]
        )
        
        num_personas = st.slider('How many personas to create?', 2, 10, 5)

# --- Main Page for Results ---

if data is None:
    st.warning("Please upload a CSV file from the sidebar to begin.")
    # st.info("💡 Tip: Use the 'Mall_Customers.csv' dataset for a great demo.")
else:
    # --- Create Tabs for a clean layout ---
    tab1, tab2, tab3 = st.tabs(["📊 Data Overview", "🧠 AI Persona Generation", "🚀 Marketing Strategy"])

    with tab1:
        st.header("Exploratory Data Analysis")
        st.dataframe(data.head())

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Data Summary")
            st.dataframe(data.describe())
        with col2:
            st.subheader("Key Metrics")
            st.metric(label="Total Customers", value=data.shape[0])
            st.metric(label="Total Attributes", value=data.shape[1])
            
        st.write("---")
        st.header("Interactive Data Visualization")
        
        col_viz1, col_viz2 = st.columns(2)
        with col_viz1:
            st.subheader("Feature Distribution")
            feature_to_plot = st.selectbox("Select a feature", numeric_columns)
            fig = px.histogram(data, x=feature_to_plot, title=f'Distribution of {feature_to_plot}', nbins=30)
            st.plotly_chart(fig, use_container_width=True)
        
        with col_viz2:
            st.subheader("Feature Relationship")
            x_axis = st.selectbox("Select X-axis", numeric_columns, index=0)
            y_axis = st.selectbox("Select Y-axis", numeric_columns, index=1)
            fig2 = px.scatter(data, x=x_axis, y=y_axis, title=f'{x_axis} vs. {y_axis}')
            st.plotly_chart(fig2, use_container_width=True)

    with tab2:
        st.header("AI-Generated Persona Results")
        if not features_for_clustering:
            st.warning("Please select features in the sidebar to create personas.")
        else:
            X = data[features_for_clustering]
            scaler = StandardScaler()
            X_scaled = scaler.fit_transform(X)
            
            kmeans = KMeans(n_clusters=num_personas, random_state=42, n_init=10)
            data['Persona'] = kmeans.fit_predict(X_scaled)
            
            st.success(f"{num_personas} personas have been successfully created!")
            
            st.subheader("Interactive Persona Visualization")
            fig3 = px.scatter(
                data,
                x=features_for_clustering[0],
                y=features_for_clustering[1] if len(features_for_clustering) > 1 else None,
                color='Persona',
                color_continuous_scale=px.colors.sequential.Viridis,
                hover_data=data.columns,
                title="Customer Segments"
            )
            st.plotly_chart(fig3, use_container_width=True)
            
            st.subheader("Data with Persona Labels")
            st.dataframe(data.head())
            
            # --- Download Button Feature ---
            @st.cache_data
            def convert_df_to_csv(df):
                return df.to_csv(index=False).encode('utf-8')

            csv_data = convert_df_to_csv(data)
            st.download_button(
               label="📥 Download Segmented Data as CSV",
               data=csv_data,
               file_name='customer_personas.csv',
               mime='text/csv',
            )

    with tab3:
        st.header("Marketing Strategy & Persona Naming")
        
        persona_summary = data.groupby('Persona')[features_for_clustering].mean().round(2)
        
        st.subheader("Persona Profile Summary")
        st.dataframe(persona_summary)
        
        st.write("---")
        st.subheader("Customize & Define Your Personas")

        # --- Dynamic Persona Naming Feature ---
        persona_names = {}
        for i in sorted(data['Persona'].unique()):
            with st.container(border=True):
                col_name, col_strat = st.columns([1, 2])
                with col_name:
                    default_name = f"Persona {i}"
                    persona_names[i] = st.text_input("Assign a Name:", value=default_name, key=f"persona_name_{i}")
                    st.dataframe(persona_summary.loc[[i]])
                
                with col_strat:
                    # This is a rule-based example. You can make this logic much more complex.
                    st.markdown(f"**Suggested Strategy for {persona_names[i]}**")
                    avg_values = persona_summary.loc[i]
                    
                    if 'Spending Score (1-100)' in avg_values and 'Annual Income (k$)' in avg_values:
                        spending = avg_values['Spending Score (1-100)']
                        income = avg_values['Annual Income (k$)']
                        
                        if spending > 65 and income > 65:
                            st.markdown("- **Profile:**  **High-Value Champions**. High income, high spenders.\n- **Strategy:** Target with premium products, loyalty programs, and exclusive offers.")
                        elif spending < 35 and income < 40:
                            st.markdown("- **Profile:**  **Budget-Conscious Savers**. Cautious spenders looking for value.\n- **Strategy:** Engage with discounts, bundle offers, and 'value for money' campaigns.")
                        elif spending > 60 and income < 40:
                            st.markdown("- **Profile:**  **Eager Young Shoppers**. Lower income but high desire to spend on trends.\n- **Strategy:** Use social media ( Instagram), influencer marketing, and 'Buy Now, Pay Later' options.")
                        else:
                            st.markdown("- **Profile:**  **Standard Customers**. Average income and spending.\n- **Strategy:** Nurture with email marketing, seasonal promotions, and a focus on customer service.")