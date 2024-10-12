PROMPT = """
You are an expert in garment attribute classification task. You will be given an image from which you have to identify the attributes listed below of the garment wore by the person in the image. Each attribute listed below is followed by the possible values. Answer to each attribute should be from the possible values only.   

1. Fabric: 
- Possible Values: Cotton, BLENDED, Polyester, Other, Nylon, Viscose Rayon, Synthetic, Cashmere, Linen, Silk, Wool, Linen Blend, Tencel, Acrylic, Modal, Ramie, Leather, Bemberg, Khadi, Brasso, Jacquard, Livaeco, Polyester PU Coated, Georgette, Organic Cotton, Bamboo, Poly Silk, Lame

2. Occasion:
- Possible Values: Casual, Formal, Party, Maternity

3. Shape:
- Possible Values: Wrap, Shirt, Fit and Flare, A-Line, Bodycon, T-Shirt, Kaftan, Maxi, Peplum, Blouson, Sheath, Pinafore, Drop Waist, Empire, Balloon, Jumper Dress, Gown, Blazer Dresses

4. Neck:
- Possible Values: V-Neck, Round Neck, Boat Neck, Halter Neck, Off-Shoulder, Strapless, Square neck, Shirt Collar, Mock Neck,One Shoulder, Cowl Neck, Mandarin Collar, Peter Pan Collar, Sweetheart Neck, Tie-Up Neck, Shoulder Straps, Keyhole Neck, Choker Neck, Hood, Asymmetric Neck, Above the keyboard Collar, High Neck

5. Pattern:
- Possible Values: Checked, Solid, Striped, Printed, Embroidered, Self Design, Embellished, Colourblocked, Dyed

6. Length:
- Possible Values: Mini, Above Knee, Knee Length, Maxi, Midi

7. Sleeve length:
- Possible Values: Long Sleeves, Short Sleeves, Sleeveless, Three-Quarter Sleeves

8. Knit or woven:
- Possible Values: Knitted, Woven, Knitted and Woven

9. Hemline:
- Possible Values: Asymmetric, Curved, Flared, Flounce, High-Low, Straight, Tulip

10. Pattern Type:
- Possible Values: Abstract, Animal, Tribal, Alphanumeric, Floral, Geometric, Graphic, Colourblocked, Polka Dots, Bohemian, Striped, Solid, Ethnic Motifs, Tropical, Converstational, Checked, Tie and Dye, Self Design, Embellished, Typography, Chevron, Camouflage, Cartoon Characters, Brand Logo, Stars, Superhero, Humour and Comic

11. Surface Styling:
- Possible Values: Cut-Outs, Embroidered, Fringed, Gathered or Pleated, Layered, Ruffles, Embellished, Sheen, Smocked, Tie-Ups, Bow, Applique, Lace Inserts, Leather or Faux Leather Trim, Lace Up, Belted, Pom Pom, Sequined, Mermaid Sequin, Corsage, Side Tape

12. Sleeve Styling:
- Possible Values: Kimono Sleeves, Batwing Sleeves, Extended Sleeves, Slit Sleeves, Cold-Shoulder Sleeves, Regular Sleeves, Cuffed Sleeves, Puff Sleeves, Cap Sleeves, Roll-up Sleeves, Flutter Sleeves, Flared Sleeves, No Sleeves, Shoulder Straps, Cape Sleeves, Bell Sleeves, Bishop Sleeves

13. Transparency:
- Possible Values: Semi-Sheer, Sheer, Opaque

14. Fabric Type:
- Possible Values: Chiffon, Georgette, Denim, Net, Lace, Crepe, Satin, Jacquard, Cotton, Linen, Knitted, Velvet, Scuba, Liva, Dobby, Corduroy, Cotton Cambric, Chambray, Schiffli

15. Lining:
- Possible Values: Has a lining, Doesn't have a lining

16. Wash Care:
- Possible Values: Hand Wash, Machine Wash, Dry Clean

17. Closure:
- Possible Values: Zip, Concealed Zip, Button, Hook and Eye

18. Add ons:
- Possible Values: Comes with a belt, Comes with a mask, None

19. Sustainability:
- Possible Values: Regular, Sustainable

Give all the above details in an JSON format as shown below            

Example output:

   {"Fabric": "Cotton",
    "Occasion": "Casual",
    "Shape": "T-Shirt",
    "Neck": "Round Neck",
    "Pattern": "Striped",
    "Length": "Above Knee",
    "Sleeve length": "Short Sleeves",
    "Knit or woven": "woven",
    "Hemline": "Straight",
    "Pattern Type": "Abstract",
    "Surface Styling": "Layered",
    "Sleeve Styling": "Regular Sleeves",
    "Transparency": "Opaque",
    "Fabric Type": "Linen",
    "Lining": "Has a lining",
    "Wash Care": "Machine Wash",
    "Closure": "Zip",
    "Add ons": "None",
    "Sustainability": "Regular"}

"""