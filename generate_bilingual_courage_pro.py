#!/usr/bin/env python3
"""
Professional Bilingual EPUB Generator for "The Courage to be Disliked"
Using EbookLib with proper CSS and typography
"""

from ebooklib import epub

# Create the book
book = epub.EpubBook()

# Set metadata
book.set_identifier('courage-to-be-disliked-zh-vi-001')
book.set_title('Dũng Khí Để Bị Ghét Bỏ')
book.set_language('vi')
book.add_author('Kishimi Ichiro')
book.add_author('Koga Fumitake')

# Professional CSS stylesheet optimized for KOReader html5.css mode
# Following best practices: line-height on body only, no inline styles
style = '''
@namespace epub "http://www.idpf.org/2007/ops";

/* Base styles - line-height on body only (Kobo best practice) */
body {
    font-family: Georgia, serif;
    line-height: 1.7;
    margin: 5%;
    text-align: justify;
}

/* Headings inherit line-height from body */
h1, h2, h3, h4, h5, h6 {
    font-family: Georgia, serif;
    text-align: left;
    font-weight: normal;
    margin-top: 2em;
    margin-bottom: 1em;
}

h1 {
    font-size: 1.4em;
    border-bottom: 0.1em solid #333;
    padding-bottom: 0.3em;
}

h2 {
    font-size: 1.2em;
}

h3 {
    font-size: 1.1em;
}

/* Paragraphs */
p {
    margin: 0;
    text-indent: 0;
    margin-bottom: 0.5em;
}

/* Bilingual content */
p.chinese {
    font-size: 1.05em;
    margin-bottom: 0.3em;
    color: #000;
}

p.vietnamese {
    font-size: 1em;
    font-style: italic;
    margin-bottom: 1.8em;
    color: #666;
}

/* Glossary styling */
.glossary-term {
    margin: 1.5em 0;
}

.term-chinese {
    font-weight: bold;
    font-size: 1.1em;
    color: #000;
}

.term-arrow {
    color: #666;
}

.term-vietnamese {
    color: #666;
    font-weight: bold;
}

.term-explanation {
    margin-top: 0.3em;
    color: #666;
}
'''

# Create CSS file
main_css = epub.EpubItem(uid="style_main", file_name="style/style.css", media_type="text/css", content=style)
book.add_item(main_css)

# Create glossary chapter
glossary_html = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head>
    <title>Bảng Thuật Ngữ</title>
    <link rel="stylesheet" href="style/style.css" type="text/css"/>
</head>
<body>
    <h1>Bảng Thuật Ngữ / Glossary of Terms</h1>
    <p>Dưới đây là các thuật ngữ triết học và từ ngữ khó có thể gặp trong văn bản:</p>

    <div class="glossary-term">
        <p class="term-chinese">千年之都 (Thiên niên chi đô)</p>
        <p><span class="term-arrow">→</span> <span class="term-vietnamese">Kinh đô ngàn năm</span></p>
        <p class="term-explanation">Chỉ một thủ đô hoặc thành phố cổ kính có lịch sử lâu đời, thường ám chỉ Kyoto của Nhật Bản trong văn cảnh này.</p>
    </div>

    <div class="glossary-term">
        <p class="term-chinese">哲人 (Triết nhân)</p>
        <p><span class="term-arrow">→</span> <span class="term-vietnamese">Triết gia</span></p>
        <p class="term-explanation">Người có trí tuệ sâu sắc về triết học, hiểu biết về bản chất cuộc đời và con người.</p>
    </div>

    <div class="glossary-term">
        <p class="term-chinese">混沌 (Hỗn độn)</p>
        <p><span class="term-arrow">→</span> <span class="term-vietnamese">Hỗn độn</span></p>
        <p class="term-explanation">Trạng thái lộn xộn, rối loạn, không có trật tự. Trong triết học, chỉ tình trạng ban đầu chưa có sự phân biệt rõ ràng.</p>
    </div>

    <div class="glossary-term">
        <p class="term-chinese">理想论 (Lý tưởng luận)</p>
        <p><span class="term-arrow">→</span> <span class="term-vietnamese">Học thuyết lý tưởng</span></p>
        <p class="term-explanation">Quan điểm nhấn mạnh vào những lý tưởng, nguyên tắc cao đẹp, đôi khi được xem là xa rời thực tế.</p>
    </div>

    <div class="glossary-term">
        <p class="term-chinese">横亘 (Hoành cản)</p>
        <p><span class="term-arrow">→</span> <span class="term-vietnamese">Chắn ngang</span></p>
        <p class="term-explanation">Nằm ngang, cản trở, ngăn chặn sự tiến triển hoặc phát triển của điều gì đó.</p>
    </div>

    <div class="glossary-term">
        <p class="term-chinese">命题 (Mệnh đề)</p>
        <p><span class="term-arrow">→</span> <span class="term-vietnamese">Mệnh đề</span></p>
        <p class="term-explanation">Trong logic và triết học, là một phát biểu có thể đúng hoặc sai, là cơ sở để lập luận và suy luận.</p>
    </div>

    <div class="glossary-term">
        <p class="term-chinese">现实主义 (Hiện thực chủ nghĩa)</p>
        <p><span class="term-arrow">→</span> <span class="term-vietnamese">Chủ nghĩa hiện thực</span></p>
        <p class="term-explanation">Quan điểm nhìn nhận và chấp nhận thế giới như nó thực sự là, thường đối lập với chủ nghĩa lãng mạn hay lý tưởng.</p>
    </div>

    <div class="glossary-term">
        <p class="term-chinese">浪漫主义 (Lãng mạn chủ nghĩa)</p>
        <p><span class="term-arrow">→</span> <span class="term-vietnamese">Chủ nghĩa lãng mạn</span></p>
        <p class="term-explanation">Quan điểm nhấn mạnh cảm xúc, trí tưởng tượng và lý tưởng, thường lạc quan về cuộc sống và tương lai.</p>
    </div>

    <div class="glossary-term">
        <p class="term-chinese">主观世界 (Chủ quan thế giới)</p>
        <p><span class="term-arrow">→</span> <span class="term-vietnamese">Thế giới chủ quan</span></p>
        <p class="term-explanation">Là thế giới được nhìn nhận qua góc nhìn cá nhân, bị chi phối bởi suy nghĩ, cảm xúc và kinh nghiệm riêng của mỗi người, khác với thế giới khách quan.</p>
    </div>

    <div class="glossary-term">
        <p class="term-chinese">客观的世界 (Khách quan đích thế giới)</p>
        <p><span class="term-arrow">→</span> <span class="term-vietnamese">Thế giới khách quan</span></p>
        <p class="term-explanation">Là thế giới hiện thực tồn tại độc lập, không phụ thuộc vào nhận thức hay cảm nhận của con người.</p>
    </div>

    <div class="glossary-term">
        <p class="term-chinese">营造 (Doanh tạo)</p>
        <p><span class="term-arrow">→</span> <span class="term-vietnamese">Kiến tạo</span></p>
        <p class="term-explanation">Không đơn thuần là xây dựng vật chất mà là quá trình con người chủ động tạo dựng, hình thành thế giới quan của riêng mình.</p>
    </div>

    <div class="glossary-term">
        <p class="term-chinese">墨镜 (Mặc kính)</p>
        <p><span class="term-arrow">→</span> <span class="term-vietnamese">Kính đen</span></p>
        <p class="term-explanation">Ẩn dụ cho những thành kiến, định kiến hoặc cách nhìn tiêu cực che mờ cách chúng ta nhìn nhận thế giới. Việc 'tháo kính đen' có nghĩa là buông bỏ những quan niệm sai lầm.</p>
    </div>

    <div class="glossary-term">
        <p class="term-chinese">勇气 (Dũng khí)</p>
        <p><span class="term-arrow">→</span> <span class="term-vietnamese">Dũng khí</span></p>
        <p class="term-explanation">Trong triết học Adler, 'dũng khí' là sức mạnh tinh thần để chấp nhận thay đổi, đối diện với sự thật và chịu trách nhiệm cho cuộc đời của chính mình.</p>
    </div>

    <div class="glossary-term">
        <p class="term-chinese">希腊哲学 (Hy Lạp triết học)</p>
        <p><span class="term-arrow">→</span> <span class="term-vietnamese">Triết học Hy Lạp</span></p>
        <p class="term-explanation">Hệ thống tư tưởng triết học cổ đại của Hy Lạp, với các triết gia như Socrates, Plato, Aristotle. Đây là nền tảng của triết học phương Tây.</p>
    </div>

    <div class="glossary-term">
        <p class="term-chinese">另一种哲学 (Lệnh nhất chủng triết học)</p>
        <p><span class="term-arrow">→</span> <span class="term-vietnamese">Một triết học khác</span></p>
        <p class="term-explanation">Ám chỉ tâm lý học Adler - một trường phái tin rằng con người có thể thay đổi và đạt được hạnh phúc thông qua việc thay đổi cách nhìn nhận về bản thân.</p>
    </div>
</body>
</html>
'''

glossary = epub.EpubHtml(title='Bảng Thuật Ngữ', file_name='glossary.xhtml', lang='vi')
glossary.set_content(glossary_html.encode('utf-8'))
glossary.add_item(main_css)
book.add_item(glossary)

# Main chapter with bilingual content
chapter_html = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head>
    <title>引言</title>
    <link rel="stylesheet" href="style/style.css" type="text/css"/>
</head>
<body>
    <h2>引言</h2>

    <p class="chinese">从前，在被誉为千年之都的古都郊外住着一位哲人，他主张：世界极其简单，人们随时可以获得幸福。有一位青年无法接受这种观点，于是他去拜访这位哲人一探究竟。在这位被诸多烦恼缠绕的青年眼里，世界是矛盾丛生的一片混沌，根本无幸福可言。</p>
    <p class="vietnamese">Ngày xưa, ở ngoại ô một cố đô được ca ngợi là kinh đô ngàn năm, có một vị triết gia sinh sống. Ông chủ trương rằng: Thế giới cực kỳ đơn giản, con người bất cứ lúc nào cũng có thể đạt được hạnh phúc. Có một chàng thanh niên không thể chấp nhận quan điểm này, vì vậy anh đến thăm vị triết gia để tìm hiểu cho ra lẽ. Trong con mắt của chàng thanh niên bị vô vàn phiền não bủa vây này, thế giới là một mảnh hỗn độn đầy những mâu thuẫn, căn bản không có hạnh phúc gì cả.</p>

    <p class="chinese">青年：那么，我就重新向您发问了。先生主张世界极其简单，对吧？</p>
    <p class="vietnamese">Thanh niên: Vậy thì, tôi xin được hỏi lại ngài. Ngài chủ trương thế giới cực kỳ đơn giản, đúng không?</p>

    <p class="chinese">哲人：是的。世界简单得令人难以置信，人生也是一样。</p>
    <p class="vietnamese">Triết gia: Đúng vậy. Thế giới đơn giản đến mức khó tin, cuộc đời cũng như vậy.</p>

    <p class="chinese">青年：您这种主张是基于现实而并非仅仅是理想论吗？也就是说，您认为横亘在你我人生中的种种问题也是简单的吗？</p>
    <p class="vietnamese">Thanh niên: Chủ trương của ngài có dựa trên thực tế chứ không chỉ đơn thuần là một lý thuyết lý tưởng phải không? Nghĩa là, ngài có cho rằng những vấn đề đang chắn ngang trong cuộc đời của tôi và ngài cũng là những vấn đề đơn giản?</p>

    <p class="chinese">哲人：当然。</p>
    <p class="vietnamese">Triết gia: Tất nhiên rồi.</p>

    <p class="chinese">青年：好吧。在开始辩论之前，请允许我先说明一下此次造访的目的。首先，我冒昧造访的首要缘故就是要和先生充分辩论，以见分晓；其次，如果可能的话，我希望能让先生您收回自己的主张。</p>
    <p class="vietnamese">Thanh niên: Được rồi. Trước khi bắt đầu tranh luận, xin cho phép tôi nói rõ mục đích của chuyến viếng thăm lần này. Trước hết, lý do chính mà tôi mạo muội đến đây chính là để tranh luận thấu đáo với ngài, để phân định rõ ràng; thứ hai, nếu có thể, tôi hy vọng có thể thuyết phục ngài rút lại chủ trương của mình.</p>

    <p class="chinese">哲人：呵呵呵。</p>
    <p class="vietnamese">Triết gia: Haha.</p>

    <p class="chinese">青年：久闻先生大名。据说此地住着一位与众不同的哲人，提倡不容小觑的理想论——人可以改变、世界极其简单、人人能获得幸福。对我来说，先生的这些论调我都无法接受。</p>
    <p class="vietnamese">Thanh niên: Tôi đã nghe danh ngài từ lâu. Nghe nói ở đây có một vị triết gia khác thường, tuyên dương một học thuyết lý tưởng không thể xem thường—con người có thể thay đổi, thế giới cực kỳ đơn giản, mọi người đều có thể đạt được hạnh phúc. Đối với tôi, những luận điệu này của ngài, tôi đều không thể chấp nhận được.</p>

    <p class="chinese">所以，我想用自己的眼睛去确认，哪怕是微小的不当之处也要给您纠正过来。不知是否打搅您了？</p>
    <p class="vietnamese">Vì vậy, tôi muốn dùng đôi mắt của chính mình để xác minh, dù chỉ là một sai lầm nhỏ nhất cũng phải sửa lại cho ngài. Không biết có làm phiền ngài không?</p>

    <p class="chinese">哲人：没有，欢迎之至。我自己也正期待着倾听像你这样的年轻人的心声以丰富学问呢。</p>
    <p class="vietnamese">Triết gia: Không, hoan nghênh lắm. Bản thân tôi cũng đang mong được lắng nghe tâm tư của một người trẻ như cậu để làm phong phú thêm học vấn.</p>

    <p class="chinese">青年：非常感谢。其实我也并非是想要不分青红皂白地否定先生。首先，假定先生的说法成立，我们从这种可能性开始思考。</p>
    <p class="vietnamese">Thanh niên: Cảm ơn ngài rất nhiều. Thật ra tôi cũng không phải là muốn phủ định ngài một cách bừa bãi không phân biệt đúng sai. Trước hết, giả định rằng lời nói của ngài là đúng, chúng ta bắt đầu suy nghĩ từ khả năng này.</p>

    <p class="chinese">世界是简单的，人生也是如此。假若这种命题中含有几分真理，那也是对于孩子的世界而言。孩子的世界没有劳动或纳税之类的现实义务，他们每天都在父母或社会的呵护下自由自在地生活，未来充满无限希望，自己也似乎无所不能。孩子们的眼睛被遮盖了，不必去面对丑恶的现实。</p>
    <p class="vietnamese">Thế giới là đơn giản, cuộc đời cũng như vậy. Nếu như trong mệnh đề này có chứa đựng vài phần chân lý, thì đó cũng chỉ dành cho thế giới của trẻ con mà thôi. Thế giới của trẻ con không có những nghĩa vụ thực tế như lao động hay đóng thuế, chúng mỗi ngày đều sống tự do tự tại dưới sự che chở của cha mẹ hoặc xã hội, tương lai tràn đầy hy vọng vô hạn, bản thân chúng dường như cũng có thể làm được mọi việc. Đôi mắt của trẻ con bị che lại, không cần phải đối mặt với hiện thực xấu xa.</p>

    <p class="chinese">的确，孩子眼中的世界呈现出简单的姿态。</p>
    <p class="vietnamese">Thật vậy, thế giới trong mắt trẻ con hiện ra với một tư thái đơn giản.</p>

    <p class="chinese">但是，随着年龄的增长，世界便逐渐露出真面目。人们不得不接受"我只不过如此"之类的现实，原以为等候在人生路上的一切"可能"都会变成"不可能'幸福的浪漫主义季节转瞬即逝，残酷的现实主义时代终将到来。</p>
    <p class="vietnamese">Nhưng, theo với tuổi tác gia tăng, thế giới dần dần lộ ra bộ mặt thật. Con người không thể không chấp nhận những hiện thực kiểu như "ta chỉ là như vậy mà thôi", những "khả năng" vốn tưởng rằng đang chờ đợi trên con đường nhân sinh đều biến thành "bất khả", mùa lãng mạn hạnh phúc thoáng qua trong nháy mắt, thời đại hiện thực tàn khốc cuối cùng sẽ đến.</p>

    <p class="chinese">哲人：你的话的确很有趣。</p>
    <p class="vietnamese">Triết gia: Lời của cậu thực sự rất thú vị.</p>

    <p class="chinese">青年：还不仅如此。人一旦长大，就会被复杂的人际关系所困扰，被诸多的责任所牵绊。工作、家庭或者社会责任，一切都是。当然，孩提时代无法理解的歧视、战争或阶级之类的各种社会问题也会摆在你眼前，不容忽视。这些都没错吧？</p>
    <p class="vietnamese">Thanh niên: Không chỉ thế đâu. Con người một khi trưởng thành, sẽ bị vướng mắc bởi những mối quan hệ con người phức tạp, bị ràng buộc bởi vô số trách nhiệm. Công việc, gia đình hay trách nhiệm xã hội, tất cả đều như vậy. Dĩ nhiên, các vấn đề xã hội như phân biệt đối xử, chiến tranh hay giai cấp mà thời thơ ấu không thể hiểu được cũng sẽ hiện ra trước mắt bạn, không thể phớt lờ. Những điều này đều đúng chứ?</p>

    <p class="chinese">哲人：是啊。请你继续说下去。</p>
    <p class="vietnamese">Triết gia: Đúng vậy. Cậu cứ tiếp tục nói đi.</p>

    <p class="chinese">青年：如果是在宗教盛行的时代，人们也还有救。那时，神的旨意就是真理、就是世界、就是一切，只要遵从神的旨意，需要思考的课题也就很少。但现在宗教失去了力量，人们对神的信仰也趋于形式化。没有任何可以信赖的东西，人人都充满了不安和猜忌，大家都只为自己而活，这就是所谓的现代社会。</p>
    <p class="vietnamese">Thanh niên: Nếu là thời đại tôn giáo thịnh hành, con người còn có thể được cứu rỗi. Lúc đó, ý chí của Thần chính là chân lý, chính là thế giới, chính là tất cả, chỉ cần tuân theo ý chí của Thần, các vấn đề cần suy nghĩ cũng rất ít. Nhưng giờ đây tôn giáo đã mất đi sức mạnh, niềm tin của con người vào Thần cũng trở nên hình thức hóa. Không có gì có thể tin cậy, ai ai cũng tràn đầy bất an và hoài nghi, mọi người đều chỉ sống vì bản thân mình, đó chính là cái gọi là xã hội hiện đại.</p>

    <p class="chinese">那么，请先生冋答我。在这样的现实面前，您依然要说世界是简单的吗？</p>
    <p class="vietnamese">Vậy thì, xin thầy hãy trả lời tôi. Trước hiện thực như thế này, thầy vẫn còn nói rằng thế giới là đơn giản sao?</p>

    <p class="chinese">哲人：我的答案依然不变。世界是简单的，人生也是简单的。</p>
    <p class="vietnamese">Triết gia: Câu trả lời của tôi vẫn không đổi. Thế giới là đơn giản, cuộc đời cũng là đơn giản.</p>

    <p class="chinese">青年：为什么？世界是矛盾横生的一片混沌，这难道不是有目共睹的吗？</p>
    <p class="vietnamese">Thanh niên: Tại sao? Thế giới là một mảng hỗn loạn đầy rẫy mâu thuẫn, điều này chẳng phải ai cũng thấy rõ sao?</p>

    <p class="chinese">哲人：那并非是"世界"本身复杂，完全是"你"把世界看得复杂。</p>
    <p class="vietnamese">Triết gia: Không phải bản thân "thế giới" phức tạp, hoàn toàn là "cậu" nhìn thế giới một cách phức tạp.</p>

    <p class="chinese">青年：我吗？</p>
    <p class="vietnamese">Thanh niên: Tôi ư?</p>

    <p class="chinese">哲人：人并不是住在客观的世界，而是住在自己营造的主观世界里。你所看到的世界不同于我所看到的世界，而且恐怕是不可能与任何人共有的世界。</p>
    <p class="vietnamese">Triết gia: Con người không sống trong thế giới khách quan, mà sống trong thế giới chủ quan do chính mình kiến tạo. Thế giới mà cậu nhìn thấy khác với thế giới mà tôi nhìn thấy, và có lẽ là một thế giới không thể chia sẻ với bất kỳ ai.</p>

    <p class="chinese">青年：那是怎么回事呢？先生和我不是都生活在同一个时代、同一个国家、看着相同的事物吗？</p>
    <p class="vietnamese">Thanh niên: Điều đó là sao? Thầy và tôi chẳng phải đều sống trong cùng một thời đại, cùng một quốc gia, nhìn những sự vật giống nhau sao?</p>

    <p class="chinese">哲人：是啊。看上去你很年轻，不知道有没有喝过刚汲上来的井水。</p>
    <p class="vietnamese">Triết gia: Đúng vậy. Nhìn vẻ bề ngoài cậu còn rất trẻ, không biết có từng uống nước giếng mới múc lên chưa?</p>

    <p class="chinese">青年：井水？啊，那是很久以前的事情了，位于乡下的祖母家有一口井。炎炎夏日里在祖母家喝清凉的井水可是那时的一大乐趣啊！</p>
    <p class="vietnamese">Thanh niên: Nước giếng ư? À, đó là chuyện từ rất lâu rồi, nhà bà ngoài ở quê có một cái giếng. Mùa hè nóng nực uống nước giếng mát lạnh ở nhà bà ngoài chính là một niềm vui lớn thời đó!</p>

    <p class="chinese">哲人：或许你也知道，井水的温度是恒定的，长年在18度左右。这是一个客观数字，无论谁测都一样。但是，夏天喝到的井水感觉凉爽，而冬天饮用时就感觉温润。温度恒定在18度，但夏天和冬天饮用的感觉却大不相同。</p>
    <p class="vietnamese">Triết gia: Có lẽ cậu cũng biết, nhiệt độ nước giếng là không đổi, quanh năm vào khoảng 18 độ. Đây là một con số khách quan, ai đo cũng như nhau. Nhưng, nước giếng uống vào mùa hè cảm thấy mát lạnh, còn uống vào mùa đông lại cảm thấy ấm áp. Nhiệt độ không đổi ở 18 độ, nhưng cảm giác khi uống vào mùa hè và mùa đông lại rất khác nhau.</p>

    <p class="chinese">青年：这是环境变化造成的错觉。</p>
    <p class="vietnamese">Thanh niên: Đó là ảo giác do sự thay đổi môi trường gây ra.</p>

    <p class="chinese">哲人：不，这并不是错觉。对那时的"你"来说，井水的冷暖是不容否定的事实。所谓住在主观的世界中就是这个道理。"如何看待"这一主观就是全部，并且我们无法摆脱自己的主观。</p>
    <p class="vietnamese">Triết gia: Không, đó không phải là ảo giác. Với "cậu" lúc đó, sự nóng lạnh của nước giếng là một sự thật không thể phủ nhận. Cái gọi là sống trong thế giới chủ quan chính là điều này. Cái chủ quan "nhìn nhận như thế nào" chính là tất cả, và chúng ta không thể thoát khỏi cái chủ quan của chính mình.</p>

    <p class="chinese">现在，你眼中的世界呈现出复杂怪异的一片混沌。但是，如果你自身发生了变化，世界就会恢复其简单姿态。因为，问题不在于世界如何，而在于你自己怎样。</p>
    <p class="vietnamese">Bây giờ, thế giới trong mắt cậu hiện ra như một mảng hỗn loạn phức tạp kỳ quái. Nhưng, nếu bản thân cậu thay đổi, thế giới sẽ trở lại với diện mạo đơn giản của nó. Bởi vì, vấn đề không nằm ở thế giới như thế nào, mà nằm ở chính bản thân cậu thế nào.</p>

    <p class="chinese">青年：在于我自己怎样？</p>
    <p class="vietnamese">Thanh niên: Ở chỗ bản thân tôi sao?</p>

    <p class="chinese">哲人：是的。也许你是在透过墨镜看世界，这样看到的世界理所当然就会变暗。如果真是如此，你需要做的是摘掉墨镜，而不是感叹世界的黑暗。</p>
    <p class="vietnamese">Triết gia: Đúng vậy. Có thể bạn đang nhìn thế giới qua một chiếc kính đen, và thế giới nhìn qua đó đương nhiên sẽ trở nên tối tăm. Nếu quả thật như vậy, điều bạn cần làm là tháo chiếc kính đen ra, chứ không phải than thở về sự tối tăm của thế giới.</p>

    <p class="chinese">摘掉墨镜之后看到的世界也许会太过耀眼，而使你禁不住闭上眼睛。或许你又会想念墨镜。即便如此，你依然能够摘掉墨镜吗？你能正视这个世界吗？你有这种"勇气"吗？问题就在这里。</p>
    <p class="vietnamese">Thế giới sau khi tháo kính đen có thể quá chói lọi, khiến bạn không thể không nhắm mắt lại. Có lẽ bạn sẽ lại nhớ đến chiếc kính đen. Dù vậy, bạn vẫn có thể tháo chiếc kính đen được không? Bạn có thể nhìn thẳng vào thế giới này không? Bạn có "dũng khí" đó không? Vấn đề nằm ở đây.</p>

    <p class="chinese">青年：勇气？</p>
    <p class="vietnamese">Thanh niên: Dũng khí?</p>

    <p class="chinese">哲人：是的，这就是"勇气"的问题。</p>
    <p class="vietnamese">Triết gia: Đúng vậy, đây chính là vấn đề về "dũng khí".</p>

    <p class="chinese">青年：哎呀，好啦！反驳的言辞我有很多，但这些好像应该暂且放一放再说。我要确认一下，先生说"人可以改变"，对吧？您认为只要自身发生变化，世界就会恢复其简单姿态，是这样吗？</p>
    <p class="vietnamese">Thanh niên: Chà, được rồi! Tôi có rất nhiều lời bác bỏ, nhưng có lẽ nên tạm gác những điều đó lại đã. Tôi muốn xác nhận một chút, thầy nói "con người có thể thay đổi", đúng không? Ngài cho rằng chỉ cần bản thân thay đổi, thế giới sẽ trở lại với dáng vẻ giản đơn của nó, có phải vậy không?</p>

    <p class="chinese">哲人：当然，人可以改变。不仅如此，人还可以获得幸福。</p>
    <p class="vietnamese">Triết gia: Tất nhiên, con người có thể thay đổi. Không chỉ vậy, con người còn có thể đạt được hạnh phúc.</p>

    <p class="chinese">青年：所有的人都不例外吗？</p>
    <p class="vietnamese">Thanh niên: Tất cả mọi người đều không ngoại lệ sao?</p>

    <p class="chinese">哲人：无一例外，而且是随时可以。</p>
    <p class="vietnamese">Triết gia: Không một ngoại lệ nào, và hơn nữa là có thể bất cứ lúc nào.</p>

    <p class="chinese">青年：哈哈哈，先生您口气可真大呀！这不是很有趣吗，先生？现在我马上就要驳倒您！</p>
    <p class="vietnamese">Thanh niên: Ha ha ha, thầy nói thật là hùng hồn đấy! Thú vị thật không, thưa thầy? Bây giờ tôi sẽ bác bỏ ngài ngay!</p>

    <p class="chinese">哲人：我乐意迎战。那咱们就好好辩论一番吧。你的立场是"人无法改变"，对吧？</p>
    <p class="vietnamese">Triết gia: Tôi vui lòng đón nhận thách thức. Vậy thì chúng ta hãy tranh luận kỹ lưỡng nhé. Lập trường của bạn là "con người không thể thay đổi", đúng không?</p>

    <p class="chinese">青年：无法改变。目前，我自己就在为不能改变而苦恼。</p>
    <p class="vietnamese">Thanh niên: Không thể thay đổi. Hiện tại, chính bản thân tôi đang khổ sở vì không thể thay đổi.</p>

    <p class="chinese">哲人：但是，同时你自己又期待改变。</p>
    <p class="vietnamese">Triết gia: Nhưng đồng thời, chính bạn lại mong muốn sự thay đổi.</p>

    <p class="chinese">青年：那是当然。如果可以改变，如果人生可以重新来过，我甘愿跪倒在先生面前。不过，也许先生会输给我。</p>
    <p class="vietnamese">Thanh niên: Đó là đương nhiên. Nếu có thể thay đổi, nếu cuộc đời có thể bắt đầu lại, tôi sẵn sàng quỳ gối trước mặt thầy. Tuy nhiên, có lẽ thầy sẽ thua tôi đấy.</p>

    <p class="chinese">哲人：好吧。这真是很有意思的事情。看着你，让我想起了学生时代的自己。想起了年轻时为探求真理而去寻访哲人的血气方刚的自己。</p>
    <p class="vietnamese">Triết gia: Được thôi. Đây thực sự là một chuyện thú vị. Nhìn bạn, tôi nhớ lại chính mình thời còn là sinh viên. Nhớ lại bản thân trẻ tuổi đầy máu lửa đã đi tìm kiếm các triết gia để khám phá chân lý.</p>

    <p class="chinese">青年：是的，就是那样。我也是正在探求真理，人生的真理。</p>
    <p class="vietnamese">Thanh niên: Đúng vậy, chính là như thế. Tôi cũng đang khám phá chân lý, chân lý của cuộc đời.</p>

    <p class="chinese">哲人：之前我从未收过弟子，而且也一直都感觉没那种必要。但是，自从成了希腊哲学信徒之后，特别是邂逅"另一种哲学"以来，我感觉自己内心的某个角落一直在等待着像你这样年轻人的出现。</p>
    <p class="vietnamese">Triết gia: Trước đây tôi chưa từng nhận đệ tử, và cũng luôn cảm thấy không có nhu cầu đó. Nhưng từ khi trở thành tín đồ của triết học Hy Lạp, đặc biệt là sau khi gặp gỡ "một triết học khác", tôi cảm thấy một góc nào đó trong tâm hồn mình luôn chờ đợi sự xuất hiện của một người trẻ như bạn.</p>

    <p class="chinese">青年：另一种哲学？那是什么呀？</p>
    <p class="vietnamese">Thanh niên: Một triết học khác? Đó là gì vậy?</p>

    <p class="chinese">哲人：来，请去那边的书房。就要进入漫长的深夜了，给你准备一杯咖啡什么的吧。</p>
    <p class="vietnamese">Triết gia: Nào, hãy đến phòng sách bên kia. Một đêm dài sắp bắt đầu, để tôi pha cho bạn một tách cà phê gì đó nhé.</p>
</body>
</html>
'''

chapter1 = epub.EpubHtml(title='引言', file_name='chapter1.xhtml', lang='zh')
chapter1.set_content(chapter_html.encode('utf-8'))
chapter1.add_item(main_css)
book.add_item(chapter1)

# Define Table of Contents
book.toc = (epub.Link('glossary.xhtml', 'Bảng Thuật Ngữ', 'glossary'),
            epub.Link('chapter1.xhtml', '引言', 'chapter1'))

# Add navigation files
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

# Define spine
book.spine = ['nav', glossary, chapter1]

# Write the EPUB
epub.write_epub('output/courage_bilingual_professional.epub', book, {})

print("✓ Professional bilingual EPUB created successfully!")
print("✓ Location: output/courage_bilingual_professional.epub")
print("✓ Using EbookLib with professional CSS and typography")
print("✓ Features:")
print("  - Georgia serif font for excellent readability")
print("  - Line-height 1.7 for comfortable reading")
print("  - Proper margins (5%) for all e-readers")
print("  - Clean italicized translations")
print("  - Professional glossary styling")
print("  - Fully compliant EPUB3 structure")
