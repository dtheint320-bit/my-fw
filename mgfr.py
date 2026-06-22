import streamlit as se

se.title("Welcome to my web design and Logo Page")
se.write("You can download Logos and Designs at the bottom of the page>:)")

m, ctvca = se.tabs(["Home", "Links"])

with m:
    mcr = '''"Transforming Ideas Into Stunning Designs

Welcome to my creative design studio, where imagination meets innovation. We specialize in creating unique visual identities that help businesses stand out and make lasting impressions.

Our Services
Logo Design

Professional, memorable, and timeless logos tailored to your brand's personality and vision.

Brand Identity

Complete branding solutions including color palettes, typography, brand guidelines, and visual systems.

Graphic Design

Eye-catching designs for social media, marketing materials, advertisements, posters, and more.

Web Design

Modern, responsive, and user-friendly website designs that enhance your online presence.

UI/UX Design

Beautiful and intuitive digital experiences focused on usability and customer satisfaction.

Why Choose?

✓ Creative and original concepts
✓ Modern and professional designs
✓ Fast turnaround times
✓ Client-focused approach
✓ Affordable pricing
✓ Unlimited dedication to quality

My Mission

I believe great design is more than just aesthetics. It tells a story, builds trust, and creates meaningful connections between brands and their audiences.

Let's Create Something Amazing

Whether you're launching a new business, refreshing your brand, or looking for high-quality design solutions, we're here to bring your vision to life.

Your Brand. Your Vision. Our Design."'''
    se.markdown(mcr)

    se.header("btw this is me;)")

    se.image("m.png")
    
    cv = '''There Are Various Types of Logos

    Every brand is unique, and choosing the
      right type of logo is an important step 
      in building a strong visual identity.
        Different logo styles communicate different
          messages and help businesses connect 
          with their target audience more effectively.

    Wordmark Logos

    Wordmark logos focus on the company name using distinctive typography. They are simple, clean, and highly memorable.

    Lettermark Logos

    Lettermark logos use initials or abbreviations to create a compact and professional brand identity.

    Symbol Logos'''
    se.markdown(cv)
    se.image("f.png")

    e = ''''Symbol logos rely on a unique icon or graphic element to represent the brand, making them instantly recognizable.

Combination Logos

Combination logos blend text and symbols together, offering flexibility and strong brand recognition.

Emblem Logos

Emblem logos feature text integrated within a badge, seal, or crest design, often conveying tradition and authority.

Mascot Logos

Mascot logos use illustrated characters to create a friendly, engaging, and memorable brand personality.

Abstract Logos

Abstract logos utilize unique geometric or artistic shapes to communicate a brand's values and identity in a creative way.

Minimalist Logos

Minimalist logos focus on simplicity, clean lines, and essential elements, creating a modern and timeless appearance.

Finding the Perfect Logo Style

The best logo style depends on your brand's goals, audience, industry, and personality. A well-designed logo not only looks attractive but also communicates your brand story and leaves a lasting impression.'''
    se.markdown(e)

    logo_sty = ["Iconic",
             "Modern",
             "Future Nexus",
             "Prime design"]

    mc = se.selectbox("select your  style", logo_sty
                 )

    if mc == logo_sty[0]:
        oe = se.image("da.jpg")
        with open("da.jpg", "rb") as mn:
            se.download_button(label= "download this file↑",
                                data= mn, file_name= "iconic.png", 
                                mime= "image/jpg")

        kc = se.image("ic.png")
        with open("ic.png", "rb") as ki:
            se.download_button(label= "download this file↑",
                                data= ki, 
                                file_name= "iconic/1.png")

        me = se.image("d.png")
        with open("d.png", "rb") as c:
            se.download_button(label= "download this file↑",
                                data= c,
                                  file_name= "iconic/2.png")


    if mc == logo_sty[1]:
        m = se.image("vcd.png")
        with open("vcd.png", "rb") as v:
            se.download_button(label= "download this files↑",
                                data= v,
                                  file_name= "modern/ds.png")
        
        kc = se.image("vc.png")
        with open("vc.png", "rb") as ki:
            se.download_button(label= "download this file↑",
                                data= ki, 
                                file_name= "modern-ds/1.png")

        mz = se.image("zl.png")
        with open("zl.png", "rb") as b:
            se.download_button(label= "download this file↑",
                                data= b,
                                  file_name= "modern-ds/2.png")


    if mc == logo_sty[2]:
        mz = se.image("k.png")
        with open("k.png", "rb") as b:
            se.download_button(label= "download this file↑",
                                data= b,
                                  file_name= "nexus-ds/2.png")

        mz = se.image("1.png")
        with open("1.png", "rb") as b:
            se.download_button(label= "download this file↑",
                                data= b,
                                  file_name= "nexus-ds/1.png")

        mz = se.image("de.png")
        with open("de.png", "rb") as era:
            se.download_button(label= "download this file↑",
                                data= era,
                                  file_name= "nexus-ds/2.png", key= "ynh")


    if mc == logo_sty[3]:
        mz = se.image("mca.png")
        with open("mca.png", "rb") as era:
            se.download_button(label= "download this file↑",
                                data= era, file_name= "mc.png")
        
        mz = se.image("car.png")
        with open("car.png", "rb") as era:
            se.download_button(label= "download this file↑",
                                data= era,
                                  file_name= "nexus-ds/2.png", key= "ynhdx")

        mz = se.image("cvx.png")
        with open("cvx.png", "rb") as era:
            se.download_button(label= "download this file↑",
                                data= era,
        
                                  file_name= "nexus-ds/2.png", key= "ynhjn")



with ctvca:                                  
    se.header("here my tiktok Link;]↓")
    uc = "https://www.tiktok.com/@kevingman3?is_from_webapp=1&sender_device=pc"
    se.page_link(uc, label= "click to view my page")