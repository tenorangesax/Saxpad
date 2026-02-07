# The Saxpad™
This is the repo for my Saxpad™, a test project to learn a bit before commiting to the R.A.P. It was my first time to ever do something like this, and took me a long time, but I'm proud of it.
It is a shortcut pad with a bare-bones design to show off all the (very cool) internals.

*****THE FINISHED PRODUCT!!!*****
<img width="1062" height="724" alt="Screenshot 2026-02-07 at 4 16 23 PM" src="https://github.com/user-attachments/assets/464f48f8-c45f-48ec-84dc-586e9078e78c" />


**INTERNALS:**
My Hackpad features a 3d printed case for the PCB that houses a XIAO-RP2040-DIP for the microcontroller, MX-Style switches for the keyboard switches, a rotary encoder switch for adjusting things with a knob, and some SK6812MINI LEDs as the backlit RGB.
<img width="1081" height="628" alt="Modded_Hackpad_Final" src="https://github.com/user-attachments/assets/692c7311-ce90-4238-921c-679159deba0a" />



**BILL OF MATERIALS:**
| Reference            | Qty | Value                | DNP | Exclude from BOM | Exclude from Board | Footprint                                                     | Datasheet                                                                  |
| -------------------- | --- | -------------------- | --- | ---------------- | ------------------ | ------------------------------------------------------------- | -------------------------------------------------------------------------- |
| D1,D2,D3,D4          | 4   | SK6812MINI           |     |                  |                    | LED_SMD:LED_SK6812MINI_PLCC4_3.5x3.5mm_P1.75mm                | https://cdn-shop.adafruit.com/product-files/2686/SK6812MINI_REV.01-1-2.pdf |
| SW12                 | 1   | RotaryEncoder_Switch |     |                  |                    | Rotary_Encoder:RotaryEncoder_Alps_EC11E-Switch_Vertical_H20mm | ~                                                                          |
| S1,S2,S3,S4          |  4  | MX-Style switches (Keyswitch)|        |                |                    | Button_Switch_Keyboard:SW_Cherry_MX_1.00u_PCB                 | ~                                                                          |
| (Not in schematic)   | 4   | White Blank DSA keycaps|     |                |                    | (Not in schematic)                                            | ~                                                                          |
| U1                   | 1   | XIAO-RP2040-DIP      |     |                  |                    | Seeed Studio XIAO Series Library:XIAO-RP2040-DIP              |                                                                            |
| (Not in schematic)   | 1   | 3D Printed Case (2 parts, top and bottom case)    |     |                  |                    | (not in schematic)           |                                                                            |


***And the screenshots...***

SCHEMATIC:
<img width="979" height="810" alt="Screenshot 2026-02-07 at 10 30 16 AM" src="https://github.com/user-attachments/assets/dc8bbabe-85d7-447f-8e2d-cb5755d142ba" />

PCB:
<img width="1062" height="724" alt="Screenshot 2026-02-07 at 5 47 20 PM" src="https://github.com/user-attachments/assets/e8f58522-c0a3-4907-8e69-9cdb65453f8a" />
<img width="1062" height="724" alt="Screenshot 2026-02-07 at 5 47 27 PM" src="https://github.com/user-attachments/assets/aeabbb0f-abba-4714-acf8-6ad5cd1c097e" />

<img width="1081" height="628" alt="Modded_Hackpad_Final" src="https://github.com/user-attachments/assets/61f65d6d-e315-4c75-96b5-b5283b1614c2" />
<img width="1081" height="628" alt="Modded_Hackpad_Final_Back" src="https://github.com/user-attachments/assets/60e5dfa3-77b0-45ac-9c69-d784cd114064" />

CASE:
<img width="1062" height="724" alt="Screenshot 2026-02-07 at 4 21 37 PM" src="https://github.com/user-attachments/assets/98217726-3225-4630-8fd1-8a80309aa965" />


