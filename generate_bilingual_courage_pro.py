#!/usr/bin/env python3
"""
Professional Bilingual EPUB Generator for "The Courage to be Disliked"
Using EbookMaker class with AI-generated cover (no hardcoded design elements)
"""

from ebook_maker import EbookMaker

# Create the book using EbookMaker class
book = EbookMaker(
    title='Dũng Khí Để Bị Ghét Bỏ',
    author='Kishimi Ichiro',
    language='vi',
    publisher='',
    description='A philosophical dialogue exploring Adlerian psychology'
)

# Add second author
book.book.add_author('Koga Fumitake')

# Create glossary
glossary_terms = [
    {
        'term': '千年之都 (Thiên niên chi đô)',
        'translation': 'Kinh đô ngàn năm',
        'explanation': 'Chỉ một thủ đô hoặc thành phố cổ kính có lịch sử lâu đời, thường ám chỉ Kyoto của Nhật Bản trong văn cảnh này.'
    },
    {
        'term': '哲人 (Triết nhân)',
        'translation': 'Triết gia',
        'explanation': 'Người có trí tuệ sâu sắc về triết học, hiểu biết về bản chất cuộc đời và con người.'
    },
    {
        'term': '混沌 (Hỗn độn)',
        'translation': 'Hỗn độn',
        'explanation': 'Trạng thái lộn xộn, rối loạn, không có trật tự. Trong triết học, chỉ tình trạng ban đầu chưa có sự phân biệt rõ ràng.'
    },
    {
        'term': '理想论 (Lý tưởng luận)',
        'translation': 'Học thuyết lý tưởng',
        'explanation': 'Quan điểm nhấn mạnh vào những lý tưởng, nguyên tắc cao đẹp, đôi khi được xem là xa rời thực tế.'
    },
    {
        'term': '横亘 (Hoành cản)',
        'translation': 'Chắn ngang',
        'explanation': 'Nằm ngang, cản trở, ngăn chặn sự tiến triển hoặc phát triển của điều gì đó.'
    },
    {
        'term': '命题 (Mệnh đề)',
        'translation': 'Mệnh đề',
        'explanation': 'Trong logic và triết học, là một phát biểu có thể đúng hoặc sai, là cơ sở để lập luận và suy luận.'
    },
    {
        'term': '现实主义 (Hiện thực chủ nghĩa)',
        'translation': 'Chủ nghĩa hiện thực',
        'explanation': 'Quan điểm nhìn nhận và chấp nhận thế giới như nó thực sự là, thường đối lập với chủ nghĩa lãng mạn hay lý tưởng.'
    },
    {
        'term': '浪漫主义 (Lãng mạn chủ nghĩa)',
        'translation': 'Chủ nghĩa lãng mạn',
        'explanation': 'Quan điểm nhấn mạnh cảm xúc, trí tưởng tượng và lý tưởng, thường lạc quan về cuộc sống và tương lai.'
    },
    {
        'term': '主观世界 (Chủ quan thế giới)',
        'translation': 'Thế giới chủ quan',
        'explanation': 'Là thế giới được nhìn nhận qua góc nhìn cá nhân, bị chi phối bởi suy nghĩ, cảm xúc và kinh nghiệm riêng của mỗi người, khác với thế giới khách quan.'
    },
    {
        'term': '客观的世界 (Khách quan đích thế giới)',
        'translation': 'Thế giới khách quan',
        'explanation': 'Là thế giới hiện thực tồn tại độc lập, không phụ thuộc vào nhận thức hay cảm nhận của con người.'
    },
    {
        'term': '营造 (Doanh tạo)',
        'translation': 'Kiến tạo',
        'explanation': 'Không đơn thuần là xây dựng vật chất mà là quá trình con người chủ động tạo dựng, hình thành thế giới quan của riêng mình.'
    },
    {
        'term': '墨镜 (Mặc kính)',
        'translation': 'Kính đen',
        'explanation': 'Ẩn dụ cho những thành kiến, định kiến hoặc cách nhìn tiêu cực che mờ cách chúng ta nhìn nhận thế giới. Việc \'tháo kính đen\' có nghĩa là buông bỏ những quan niệm sai lầm.'
    },
    {
        'term': '勇气 (Dũng khí)',
        'translation': 'Dũng khí',
        'explanation': 'Trong triết học Adler, \'dũng khí\' là sức mạnh tinh thần để chấp nhận thay đổi, đối diện với sự thật và chịu trách nhiệm cho cuộc đời của chính mình.'
    },
    {
        'term': '希腊哲学 (Hy Lạp triết học)',
        'translation': 'Triết học Hy Lạp',
        'explanation': 'Hệ thống tư tưởng triết học cổ đại của Hy Lạp, với các triết gia như Socrates, Plato, Aristotle. Đây là nền tảng của triết học phương Tây.'
    },
    {
        'term': '另一种哲学 (Lệnh nhất chủng triết học)',
        'translation': 'Một triết học khác',
        'explanation': 'Ám chỉ tâm lý học Adler - một trường phái tin rằng con người có thể thay đổi và đạt được hạnh phúc thông qua việc thay đổi cách nhìn nhận về bản thân.'
    }
]

book.add_glossary(glossary_terms, title='Bảng Thuật Ngữ / Glossary of Terms')

# Add bilingual chapter content
bilingual_content = [
    ('从前，在被誉为千年之都的古都郊外住着一位哲人，他主张：世界极其简单，人们随时可以获得幸福。有一位青年无法接受这种观点，于是他去拜访这位哲人一探究竟。在这位被诸多烦恼缠绕的青年眼里，世界是矛盾丛生的一片混沌，根本无幸福可言。',
     'Ngày xưa, ở ngoại ô một cố đô được ca ngợi là kinh đô ngàn năm, có một vị triết gia sinh sống. Ông chủ trương rằng: Thế giới cực kỳ đơn giản, con người bất cứ lúc nào cũng có thể đạt được hạnh phúc. Có một chàng thanh niên không thể chấp nhận quan điểm này, vì vậy anh đến thăm vị triết gia để tìm hiểu cho ra lẽ. Trong con mắt của chàng thanh niên bị vô vàn phiền não bủa vây này, thế giới là một mảnh hỗn độn đầy những mâu thuẫn, căn bản không có hạnh phúc gì cả.'),

    ('青年：那么，我就重新向您发问了。先生主张世界极其简单，对吧？',
     'Thanh niên: Vậy thì, tôi xin được hỏi lại ngài. Ngài chủ trương thế giới cực kỳ đơn giản, đúng không?'),

    ('哲人：是的。世界简单得令人难以置信，人生也是一样。',
     'Triết gia: Đúng vậy. Thế giới đơn giản đến mức khó tin, cuộc đời cũng như vậy.'),

    ('青年：您这种主张是基于现实而并非仅仅是理想论吗？也就是说，您认为横亘在你我人生中的种种问题也是简单的吗？',
     'Thanh niên: Chủ trương của ngài có dựa trên thực tế chứ không chỉ đơn thuần là một lý thuyết lý tưởng phải không? Nghĩa là, ngài có cho rằng những vấn đề đang chắn ngang trong cuộc đời của tôi và ngài cũng là những vấn đề đơn giản?'),

    ('哲人：当然。',
     'Triết gia: Tất nhiên rồi.'),

    ('青年：好吧。在开始辩论之前，请允许我先说明一下此次造访的目的。首先，我冒昧造访的首要缘故就是要和先生充分辩论，以见分晓；其次，如果可能的话，我希望能让先生您收回自己的主张。',
     'Thanh niên: Được rồi. Trước khi bắt đầu tranh luận, xin cho phép tôi nói rõ mục đích của chuyến viếng thăm lần này. Trước hết, lý do chính mà tôi mạo muội đến đây chính là để tranh luận thấu đáo với ngài, để phân định rõ ràng; thứ hai, nếu có thể, tôi hy vọng có thể thuyết phục ngài rút lại chủ trương của mình.'),
]

book.add_bilingual_chapter(
    title='引言',
    text_pairs=bilingual_content,
    original_lang='zh',
    translation_lang='vi'
)

# Save with AI-generated cover (no hardcoded subtitle)
# The AI will detect "courage" and "dũng" in the title and choose philosophical theme
output_file = 'output/courage_bilingual_professional.epub'
book.save(output_file, auto_generate_cover=True)

print("\n" + "="*60)
print("✓ Professional bilingual EPUB created successfully!")
print("="*60)
print(f"✓ Location: {output_file}")
print("\n✓ Features:")
print("  - AI-generated cover (philosophical theme)")
print("  - Color scheme auto-selected from title keywords")
print("  - No hardcoded design elements")
print("  - Georgia serif typography throughout")
print("  - Professional word-wrapping and layout")
print("  - Line-height 1.7 for comfortable reading")
print("  - Proper margins (5%) for all e-readers")
print("  - Clean italicized bilingual translations")
print("  - Professional glossary styling")
print("  - Fully compliant EPUB3 structure")
print("="*60)
