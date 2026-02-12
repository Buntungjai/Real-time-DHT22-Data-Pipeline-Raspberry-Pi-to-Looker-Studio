# Real-time-DHT22-Data-Pipeline-Raspberry-Pi-to-Looker-Studio

<p align="center">
  <img src="images/pi4dht22.png" width="400">
</p>
อุปกรณ์ที่ใช้ในโปรเจคนี้มี raspberry pi 4 และ dht22 <br>

<p align="center">
  <img src="images/VScode.jpg" width="800">
</p>
แสดงการออกแบบ Workflow บน Node-RED เพื่อรับข้อมูลจาก Raspberry Pi ผ่านโพรโทคอล MQTT โดยมีการใช้โหนด JSON และ Function (JavaScript) เพื่อจัดระเบียบข้อมูล (Data Transformation) ก่อนส่งผ่าน Google Sheets API เข้าสู่ฐานข้อมูลบนคลาวด์แบบอัตโนมัติ
<p align="center">
  <img src="images/nodeRed.jpg" width="800">
</p>

<p align="center">
  <img src="images/googlesheet.jpg" width="800">
</p>
ข้อมูลเซนเซอร์ที่ถูกบันทึกแบบ Real-time ลงบน Google Sheets
<p align="center">
  <img src="images/lookerstudio.jpg" width="800">
</p>

Business Intelligence (BI) Dashboard for Monitoring "รายงานข้อมูลเชิงวิเคราะห์ (Dashboard) ผ่าน Google Looker Studio ที่เชื่อมต่อกับฐานข้อมูลโดยตรง
