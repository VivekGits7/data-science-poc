---
  HW stands for Hardware ID - it's the unique identifier for the physical shoe device.
  PPG = Photoplethysmography
  1. Raw Data File - Patterns Found

  The file has 108,731 lines, each line is one JSON message. There are 3 types of messages in the file:

  ---
  Pattern 1: BL - Left Shoe Motion Data (lines 1-1600+)

  This is the most common pattern. Comes from the left shoe via topic: "PPG".

  topic:   "PPG"
  T:       "BL"  (Body Left)

  Fields:

  ┌───────────┬─────────────────────────────────────┬───────────────────────────────────────────────────┐
  │   Field   │               Example               │                      Meaning                      │
  ├───────────┼─────────────────────────────────────┼───────────────────────────────────────────────────┤
  │ AC        │ [-0.04, 0, 0, -0.03, -0.01, 0, ...] │ Accelerometer - 36 values = 12 samples of (x,y,z) │
  ├───────────┼─────────────────────────────────────┼───────────────────────────────────────────────────┤
  │ GY        │ [-4, -1, 0, -4, -1, 0, ...]         │ Gyroscope - 36 values = 12 samples of (x,y,z)     │
  ├───────────┼─────────────────────────────────────┼───────────────────────────────────────────────────┤
  │ BT        │ 85                                  │ Battery level (%)                                 │
  ├───────────┼─────────────────────────────────────┼───────────────────────────────────────────────────┤
  │ FP        │ 1 or 0                              │ 1 = offline/buffered, 0 = real-time               │
  ├───────────┼─────────────────────────────────────┼───────────────────────────────────────────────────┤
  │ PC        │ 4045                                │ Packet counter                                    │
  ├───────────┼─────────────────────────────────────┼───────────────────────────────────────────────────┤
  │ counter   │ 0                                   │ Internal device counter                           │
  ├───────────┼─────────────────────────────────────┼───────────────────────────────────────────────────┤
  │ DT        │ 1                                   │ Data type flag                                    │
  ├───────────┼─────────────────────────────────────┼───────────────────────────────────────────────────┤
  │ timestamp │ "2026-02-11T15:13:49.018Z"          │ When the sensor actually recorded it              │
  └───────────┴─────────────────────────────────────┴───────────────────────────────────────────────────┘

  ---
  Pattern 2: BR - Right Shoe Motion Data (starts ~line 1602)

  Comes from the right shoe via topic: "BPST_RIGHT". Has a nested Data object (different structure than BL).

  topic:   "BPST_RIGHT"
  T:       "BR"  (Body Right)

  Fields:

  ┌────────────────┬────────────────────────────┬──────────────────────────────────────────────┐
  │     Field      │          Example           │                   Meaning                    │
  ├────────────────┼────────────────────────────┼──────────────────────────────────────────────┤
  │ Data.AC        │ [-0.23, 0.08, -0.21, ...]  │ Accelerometer (same 36-value triplet format) │
  ├────────────────┼────────────────────────────┼──────────────────────────────────────────────┤
  │ Data.GY        │ [-1, 73, -1, ...]          │ Gyroscope (same format)                      │
  ├────────────────┼────────────────────────────┼──────────────────────────────────────────────┤
  │ Data.BT        │ 34                         │ Battery level                                │
  ├────────────────┼────────────────────────────┼──────────────────────────────────────────────┤
  │ Data.timestamp │ "2026-02-12T07:40:10.443Z" │ Event time                                   │
  ├────────────────┼────────────────────────────┼──────────────────────────────────────────────┤
  │ Data.Spo2      │ null                       │ SpO2 sensor (not used on right shoe)         │
  ├────────────────┼────────────────────────────┼──────────────────────────────────────────────┤
  │ Data.Pulse     │ null                       │ Pulse sensor (not used on right shoe)        │
  ├────────────────┼────────────────────────────┼──────────────────────────────────────────────┤
  │ Data.FP        │ null                       │ Connectivity flag (null in this shoe)        │
  └────────────────┴────────────────────────────┴──────────────────────────────────────────────┘

  Key difference: BR wraps sensor data inside a Data object and has extra null fields (Spo2, Pulse, Battery, Time).

  ---
  Pattern 3: PG - PPG (Heart Rate) Data (starts ~line 7322)

  Comes from the left shoe only via topic: "PPG". Contains optical sensor data instead of motion.

  topic:   "PPG"
  T:       "PG"  (PPG/Photoplethysmography)

  Fields:

  ┌───────────┬──────────────────────────────┬──────────────────────────────────────────┐
  │   Field   │           Example            │                 Meaning                  │
  ├───────────┼──────────────────────────────┼──────────────────────────────────────────┤
  │ IR        │ [82383, 107802, 107962, ...] │ Infrared light readings (for heart rate) │
  ├───────────┼──────────────────────────────┼──────────────────────────────────────────┤
  │ RD        │ [76248, 87049, 87047, ...]   │ Red light readings (for SpO2)            │
  ├───────────┼──────────────────────────────┼──────────────────────────────────────────┤
  │ PC        │ 4048                         │ Packet counter                           │
  ├───────────┼──────────────────────────────┼──────────────────────────────────────────┤
  │ BT        │ 16                           │ Battery level                            │
  ├───────────┼──────────────────────────────┼──────────────────────────────────────────┤
  │ FP        │ 0                            │ Real-time flag                           │
  ├───────────┼──────────────────────────────┼──────────────────────────────────────────┤
  │ timestamp │ "2026-02-12T07:40:10.537Z"   │ Event time                               │
  └───────────┴──────────────────────────────┴──────────────────────────────────────────┘

  No AC or GY in this type - it's purely optical sensor data.

  ---
  Other Patterns Noticed

  ┌──────────────────┬─────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
  │     Pattern      │                                                   Detail                                                    │
  ├──────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ All same user    │ Every line has userId: "Rn2Ywi"                                                                             │
  ├──────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ Same device      │ HW: "HW-mj5cxv3u-nptgqw" throughout                                                                         │
  ├──────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ Two time periods │ First batch is FP=1 (offline) from 2026-02-11 15:13, second batch is FP=0 (real-time) from 2026-02-12 07:39 │
  ├──────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ Array size = 36  │ AC and GY always have 36 values = 12 sensor samples per packet                                              │
  ├──────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ IR/RD size = 35  │ PPG arrays have ~35 values per packet                                                                       │
  ├──────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
  │ Battery drain    │ Battery goes from 85% (early data) down to 16% (later data)                                                 │
  └──────────────────┴─────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

  ---
  2. PDF Specification - Explained Simply

  Think of this system as smart shoes with sensors. Here's what's happening in plain language:

  What is this?

  Two shoes (left and right) have sensors inside them. They collect body movement and heart-related data and send it to a server.

  The Two Shoes

  ┌────────────┬──────────────────────────────────────────────────────────────────────────┬─────────────┐
  │    Shoe    │                             What it collects                             │ Stream name │
  ├────────────┼──────────────────────────────────────────────────────────────────────────┼─────────────┤
  │ Left shoe  │ Movement (walking, running, steps) + Heart signals (pulse, blood oxygen) │ PPG         │
  ├────────────┼──────────────────────────────────────────────────────────────────────────┼─────────────┤
  │ Right shoe │ Movement only                                                            │ BPST_RIGHT  │
  └────────────┴──────────────────────────────────────────────────────────────────────────┴─────────────┘

  The 3 Types of Data

  BL (Body Left) - "How is the left foot moving?"
  - Accelerometer (AC): Measures how fast the foot is speeding up or slowing down in 3 directions (left-right, forward-back, up-down). Like
   the sensor that rotates your phone screen.
  - Gyroscope (GY): Measures how the foot is rotating/twisting. Like how a game controller knows you tilted it.
  - Both come as groups of 3 numbers: (x, y, z) repeated 12 times per packet.

  BR (Body Right) - "How is the right foot moving?"
  - Same accelerometer + gyroscope data as BL, but for the right foot.
  - Same (x, y, z) triplet format.

  PG (PPG) - "What's the heart doing?"
  - IR (Infrared): Shines infrared light through skin to detect blood flow. Used to calculate heart rate.
  - RED (RD): Shines red light through skin. Combined with IR, it calculates blood oxygen level (SpO2).
  - This is the same technology your smartwatch uses for heart rate.

  The FP Flag - Online vs Offline

  - FP = 0: The shoe is connected to the phone/server right now and sending data live
  - FP = 1: The shoe was disconnected (maybe phone was far away). It saved data locally and sent it all later when reconnected. This is
  like how your fitness tracker syncs old data when you open the app.

  Why timestamp Matters

  Because offline data (FP=1) arrives late, the messages may arrive out of order. Always use timestamp (when the sensor actually recorded
  it) to sort the data, not when the server received it.

  Battery (BT)

  Simple percentage showing how much battery is left in the shoe. Useful to know when to charge.