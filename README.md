# The Saxpad™
This is the repo for my Saxpad™, a test project to learn a bit before commiting to the R.A.P. It was my first time to ever do something like this, and took me a long time, but I'm proud of it.
It is a shortcut pad with a bare-bones design to show off all the (very cool) internals.

*THE FINISHED PRODUCT!!!*
<img width="1062" height="724" alt="Screenshot 2026-02-07 at 4 16 23 PM" src="https://github.com/user-attachments/assets/464f48f8-c45f-48ec-84dc-586e9078e78c" />


**INTERNALS:**
My Hackpad features a 3d printed case for the PCB that houses a XIAO-RP2040-DIP for the microcontroller, MX-Style switches for the keyboard switches, a rotary encoder switch for adjusting things with a knob, and some SK6812MINI LEDs as the backlit RGB.
<img width="1081" height="628" alt="Modded_Hackpad_Final" src="https://github.com/user-attachments/assets/7d144992-db97-46de-93a7-5b77e9c1ebc7" />



**BILL OF MATERIALS:**
| Reference            | Qty | Value                | DNP | Exclude from BOM | Exclude from Board | Footprint                                                     | Datasheet                                                                  |
| -------------------- | --- | -------------------- | --- | ---------------- | ------------------ | ------------------------------------------------------------- | -------------------------------------------------------------------------- |
| D1,D2,D3,D4          | 4   | SK6812MINI           |     |                  |                    | LED_SMD:LED_SK6812MINI_PLCC4_3.5x3.5mm_P1.75mm                | https://cdn-shop.adafruit.com/product-files/2686/SK6812MINI_REV.01-1-2.pdf |
| (Not in schematic         | 1   | Rotary Encoder Switch Knob (3 pieces)           |     |                  |                    |(Not in schematic)                | [https://cdn-shop.adafruit.com/product-files/2686/SK6812MINI_REV.01-1-2.pdf](https://www.alibaba.com/product-detail/Rotary-15mm-High-17mm-Aluminum-Shell_60628365487.html?spm=a2700.galleryofferlist.normal_offer.d_image.596b13a07ZdWbL&priceId=b9b46d351eb74acaa07c5dc284613b05) |
| SW12                 | 1   | RotaryEncoder_Switch |     |                  |                    | Rotary_Encoder:RotaryEncoder_Alps_EC11E-Switch_Vertical_H20mm | ~                                                                          |
| S1,S2,S3,S4          |  4  | MX-Style switches (Keyswitch)|        |                |                    | Button_Switch_Keyboard:SW_Cherry_MX_1.00u_PCB                 | ~                                                                          |
| (Not in schematic)   | 4   | White Blank DSA keycaps|     |                |                    | (Not in schematic)                                            | ~                                                                          |
| U1                   | 1   | XIAO-RP2040-DIP      |     |                  |                    | Seeed Studio XIAO Series Library:XIAO-RP2040-DIP              |                                                                            |
| (Not in schematic)   | 1   | 3D Printed Case (2 parts, top and bottom case, sunset yellow prefered)    |     |                  |                    | (not in schematic)           |                                                                            |


***And the screenshots...***

SCHEMATIC:
<img width="979" height="810" alt="Schematic" src="https://github.com/user-attachments/assets/fc35afa9-f8c0-41a4-9dbe-81f9a8afbf02" />

PCB:
<img width="1062" height="724" alt="Screenshot 2026-02-07 at 5 47 20 PM" src="https://github.com/user-attachments/assets/e8f58522-c0a3-4907-8e69-9cdb65453f8a" />
<img width="1062" height="724" alt="Screenshot 2026-02-07 at 5 47 27 PM" src="https://github.com/user-attachments/assets/aeabbb0f-abba-4714-acf8-6ad5cd1c097e" />

<img width="1081" height="628" alt="Modded_Hackpad_Final" src="https://github.com/user-attachments/assets/64999e5f-f571-448d-a8d1-13f1093a7427" />
<img width="1081" height="628" alt="Modded_Hackpad_Final_Back" src="https://github.com/user-attachments/assets/60e5dfa3-77b0-45ac-9c69-d784cd114064" />

CASE:
<img width="1222" height="780" alt="Saxpad_Full_Case_Picture" src="https://github.com/user-attachments/assets/da0eab37-8f45-4e06-9978-d9664f3caeb5" />

