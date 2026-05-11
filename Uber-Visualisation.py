import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st
import plotly.express as px


df=pd.read_csv("ncr_ride_bookings.csv")
pd.set_option('display.max_columns', 21)

df['DateTime']= pd.to_datetime(df['Date']+' '+df['Time'])
df.drop(columns =['Date', 'Time'], inplace=True)

df['Reason for cancelling by Customer'] = df['Reason for cancelling by Customer'].fillna("Not Added")
df['Driver Cancellation Reason'] = df['Driver Cancellation Reason'].fillna("Not Added")
df = df.fillna('Not added')

cols_to_clean = ['Booking ID', 'Customer ID', 'Vehicle Type']
for col in cols_to_clean:
    df[col] = df[col].str.replace('"', '').str.strip()

df['Booking Value'] = pd.to_numeric(df['Booking Value'], errors='coerce')
care_value = df.groupby('Vehicle Type')['Booking Value'].sum()
care_value_ascending = care_value.sort_values(ascending=False)

df['Hour'] = df['DateTime'].dt.hour
hourly_counts = df['Hour'].value_counts().sort_index()

Pickup_localisation = df['Pickup Location'].value_counts().head(10)

df['Route'] =df['Pickup Location'] + ' => ' +df['Drop Location']
Route = df['Route'].value_counts().head()

df['Price_Per_KM']=df['Booking Value']/df['Ride Distance']
df.groupby('Vehicle Type')['Price_Per_KM'].mean()

df['Booking Value'] = pd.to_numeric(df['Booking Value'], errors='coerce').fillna(0)
df['Ride Distance'] = pd.to_numeric(df['Ride Distance'], errors='coerce').fillna(0)

numeric_df = df[['Booking Value', 'Ride Distance']]

corr_matrix = numeric_df.corr()


st.set_page_config(page_title= "Uber Ride Bookings Analysis",
                   page_icon= 'images.png',
                   layout="wide",
                   initial_sidebar_state="expanded"
                   )

st.markdown("""
<style>
    /* 1. تنظيف شامل للقائمة وإزالة الخط الفاصل المزعج */
    div[data-baseweb="tab-list"] {
        display: flex;
        justify-content: center;
        width: 100%;
        gap: 40px; /* مسافة أوسع لإعطاء فخامة */
        background-color: transparent !important;
        border-bottom: none !important; /* حذف الخط الفاصل نهائياً */
        padding: 10px 0 !important;
    }

    /* إخفاء الخط المتحرك الافتراضي لستريم ليت لضمان عدم التداخل */
    div[data-baseweb="tab-highlight"] {
        display: none !important;
    }

    /* 2. تنسيق التبويب (الحالة العادية - مدمجة تماماً) */
    button[data-baseweb="tab"] {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        padding: 10px 15px !important;
        transition: all 0.2s ease-out !important; /* تسريع الحركة ليكون ديناميكياً */
        position: relative !important;
    }

    button[data-baseweb="tab"] p {
        font-size: 19px !important; /* خط أوضح */
        color: #64748b !important; /* لون رمادي هادئ يندمج مع الخلفية */
        transition: all 0.2s ease !important;
    }

    /* 3. تأثير التبويب النشط (The Dynamic Glow) */
    button[aria-selected="true"] {
        background: transparent !important;
        transform: scale(1.1) !important; /* تكبير بسيط وناعم */
    }

    button[aria-selected="true"] p {
        color: #FFFFFF !important; /* أبيض ناصع */
        font-weight: 800 !important;
        /* تأثير الضوء (Glow) خلف النص المختار */
        text-shadow: 0px 0px 15px rgba(39, 110, 241, 0.8), 
                     0px 0px 30px rgba(39, 110, 241, 0.4) !important;
    }

    /* الخط السفلي العصري تحت التبويب المختار فقط */
    button[aria-selected="true"]::after {
        content: "";
        position: absolute;
        bottom: -5px;
        left: 20%;
        width: 60%;
        height: 4px;
        background: linear-gradient(90deg, transparent, #276EF1, transparent);
        border-radius: 2px;
    }

    /* 4. حركة تمرير الماوس (ناعمة وسريعة) */
    button[data-baseweb="tab"]:hover p {
        color: #FFFFFF !important;
        transform: translateY(-2px);
    }

    /* 5. حل مشكلة "القص" عند الضغط (إزالة الـ Focus Ring) */
    button:focus {
        outline: none !important;
        box-shadow: none !important;
    }

    /* تنسيق المحتوى داخل التبويب ليكون مدمجاً */
    .stTabs [data-baseweb="tab-panel"] {
        padding-top: 40px !important;
        background-color: transparent !important;
    }
</style>
""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs(['Car Booking Trends ', 'Rush Hour', 'Booking Status', 'Pickup Locations', 'Correlation Bookings & Distance'])
with tab1:
     st.header("Car Booking Trends")
     with st.container(border= True):
      col1, col2, col3 = st.columns(3)
     with col1:
         st.metric("Total Bookings", f"{len(df)}")
     with col2:
         st.metric("Total Booking Value", f"${df['Booking Value'].sum():,.2f}")
     with col3:
         st.metric("Average Booking Value", f"${df['Booking Value'].mean():,.2f}")
     with st.container(border= True):
      st.write("Total Booking Value by Vehicle Type:", care_value_ascending)
     with st.container(border= True):
      fig_car_value = px.bar(y= care_value_ascending.index,
                       x= care_value_ascending.values,
                       orientation = 'h',
                       title = 'The most Profitable Cars',
                       labels={'x':'Booking Value', 'y':'Cars'},
                       color=care_value_ascending.index
                       )
      st.plotly_chart(fig_car_value)
with tab2:
     st.header("Rush Hour Analysis")
     with st.container(border= True):
      col1, col2, col3 = st.columns(3)
     with col1:
            st.metric("Busiest Hour", f"{hourly_counts.idxmax()}:00 - {hourly_counts.idxmax()+1}:00")
     with col2:
            st.metric("Number of Trips in Busiest Hour", f"{hourly_counts.max()}")
     with col3:
            st.metric("Average Trips per Hour", f"{hourly_counts.mean():.2f}")
     with st.container(border= True):
      fig_rush_hour = px.line(x= hourly_counts.index,
                        y=hourly_counts.values,
                        title = 'Rush Hour Analysis',
                        labels={'x':'Hours of day', 'y':'Number of trips'},
                        color_discrete_sequence=['blue'],
                        markers = True
                        )
      st.plotly_chart(fig_rush_hour)
with tab3:
        st.header("Booking Status")
        with st.container(border= True):
         col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Cancellations", "35.5K")
        with col2:
            st.metric("Cancellation Rate", "23,66%")
        with col3:            
            st.metric("Most Common Cancellation Reason", "Not Added")
        df['Booking Status'].value_counts(normalize =True)
        Booking_Satatus = df['Booking Status'].value_counts()
        with st.container(border= True):
         fig_booking_status = px.bar(y = Booking_Satatus.index,
                           x = Booking_Satatus.values,
                           orientation = 'h',
                           title = 'Booking Status Analysis',
                           labels={'x':'Number of bookings', 'y':'Booking Status'},
                           color=Booking_Satatus.index
                           )
         st.plotly_chart(fig_booking_status)
        with st.container(border= True):
         st.expander("Reason for cancelling by Customer").write(df['Reason for cancelling by Customer'].value_counts())
with tab4:
        st.header("Pickup Locations")
        with st.container(border= True):
         col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Most Common Pickup Location", f"{Pickup_localisation.idxmax()}")
        with col2:
            st.metric("Number of Pickups at Most Common Location", f"{Pickup_localisation.max()}")
        with col3:
            st.metric("Average Pickups per Location", f"{Pickup_localisation.mean():.2f}")
        with st.container(border= True):
         fig_pickup_location = px.bar(y = Pickup_localisation.index,
                            x = Pickup_localisation.values,
                            orientation = 'h',
                            title = 'Top 10 Pickup Locations',
                            labels={'x':'Number of pickups', 'y':'Pickup Location'},
                            color=Pickup_localisation.index
                            )
         st.plotly_chart(fig_pickup_location)
        with st.container(border= True):
         fig_route = px.bar(y = Route.index,
                   x = Route.values,
                   orientation = 'h',
                   title = 'Top 5 Routes',
                   labels={'x':'Number of trips', 'y':'Route'},
                   color=Route.index
                   )
         st.plotly_chart(fig_route)
with tab5:
        st.header("Correlation between Booking Value and Ride Distance")
        with st.container(border= True):
         col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Correlation Coefficient", f"{corr_matrix.loc['Booking Value', 'Ride Distance']:.2f}")
        with col2:
            st.metric("Average Price Per KM", f"${df['Price_Per_KM'].mean():.2f}")
        with col3:
            st.metric("Most Expensive Vehicle Type", f"{df.groupby('Vehicle Type')['Price_Per_KM'].mean().idxmax()}")
        with st.container(border= True):
         st.expander("Average Price Per KM by Vehicle Type").write(df.groupby('Vehicle Type')['Price_Per_KM'].mean())
        with st.container(border= True):
         fig_corr= px.imshow(corr_matrix,
            text_auto=True,
           title='Correlation Matrix of Booking Value and Ride Distance',
           color_continuous_scale='RdBu',)
         st.plotly_chart(fig_corr)