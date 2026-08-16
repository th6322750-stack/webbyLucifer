# Asset-First Implementation-Ready UI Protocol — webbyLucifer v3.0

This is the detailed canonical tree for projects where UI fidelity is the highest priority and the implementation executor must not invent design or assets.

User-facing rule: whenever an English/specialist term is material to the explanation, explain in plain Vietnamese what it means and what it is used for.

```text
DỰ ÁN WEBSITE
|
|----- GĐ0. KHỞI ĐỘNG / KIỂM TRA ĐẦU VÀO + MÔI TRƯỜNG
|      |
|      |----- ChatGPT đọc toàn bộ dữ kiện đã có trước khi hỏi
|      |      |----- tin nhắn người dùng
|      |      |----- ảnh / PDF / Figma / video / website tham chiếu
|      |      |----- logo / font / màu / nội dung
|      |      |----- repo / code / dữ liệu / CMS nếu đã có
|      |
|      |----- Xác nhận môi trường triển khai
|      |      |----- GitHub repo nào?
|      |      |----- Branch nào?
|      |      |----- Claude đã có quyền repo chưa?
|      |      |----- ChatGPT đọc được remote repo chưa?
|      |      |----- Claude có local unpushed khác remote không?
|      |      |----- Google Drive đã kết nối + Claude tải được chưa?
|      |      |----- Có cần Vercel preview không?
|      |      |----- CMS / Sheets / API / Database ở đâu?
|      |      |----- env/secrets nào ảnh hưởng việc chạy thật?
|      |
|      |----- Xác nhận authority đầu vào
|      |      |----- reference nào là chuẩn chính?
|      |      |----- source thật nào không được bịa?
|      |
|      |----- Xác nhận bố cục lớn
|      |      |----- FULL_WIDTH?
|      |      |----- FULL_BLEED_WITH_CONTAINER?
|      |      |----- BOXED?
|      |      |----- MIXED?
|      |
|      |----- Nếu reference không đủ để biết bố cục lớn
|             |----- HỎI NGƯỜI DÙNG
|             |----- KHÔNG tự mặc định
|
|----- GĐ1. PHÂN TÍCH HƯỚNG UI / VISUAL DIRECTION
|      |
|      |----- ChatGPT = Design/UI Authority
|      |----- User = người duyệt cuối
|      |----- Claude chưa tham gia thiết kế
|      |
|      |----- Phân tích
|      |      |----- hierarchy / thứ bậc thị giác
|      |      |----- typography / font + cấp chữ
|      |      |----- color / màu
|      |      |----- spacing / khoảng cách
|      |      |----- container / vùng nội dung
|      |      |----- full-width / full-bleed / boxed
|      |      |----- card / gallery / hero / footer
|      |      |----- business priority / phần kinh doanh ưu tiên
|      |      |----- mobile / desktop intent
|      |      |----- motion intent nếu cần
|      |
|      |----- Chốt route + section cần thiết
|
|----- GĐ2. PHÂN RÃ UI + ASSET COUNT PLAN
|      |
|      |----- KHÔNG tạo asset ngay
|      |----- KHÔNG render final bằng asset chưa tồn tại
|      |
|      |----- Mỗi route
|      |      |----- liệt kê section
|      |      |----- mỗi section liệt kê số item visible/required
|      |      |----- xác định asset role
|      |
|      |----- Đếm asset theo role
|      |      |----- HERO
|      |      |----- PROJECT_CARD
|      |      |----- PROJECT_GALLERY
|      |      |----- RENTAL_CARD
|      |      |----- RENTAL_GALLERY
|      |      |----- NEWS_COVER
|      |      |----- ABOUT / CONTACT
|      |      |----- LIFESTYLE / AMENITY
|      |      |----- BRAND / LOGO / ICON
|      |      |----- FLOORPLAN / MAP / PROGRESS
|      |      |----- PLACEHOLDER
|      |
|      |----- Xác định cho từng asset
|      |      |----- asset đã có?
|      |      |----- ChatGPT tạo/chuẩn bị?
|      |      |----- bắt buộc người dùng/khách cung cấp vì không được bịa?
|      |      |----- FHD-class hay 4K-class master?
|      |      |----- vector nếu là logo/icon?
|      |      |----- cần desktop/mobile riêng hay dùng cùng master?
|      |
|      |----- BÁO NGƯỜI DÙNG TRƯỚC KHI SẢN XUẤT
|             |----- tổng asset = XX
|             |----- có sẵn = XX
|             |----- ChatGPT tạo/productionize = XX
|             |----- cần người dùng cung cấp = XX
|             |----- 4K = XX
|             |----- FHD = XX
|             |----- vector = XX
|
|----- GĐ3. PHÂN LOẠI ASSET
|      |
|      |----- BRAND
|      |      |----- logo / wordmark / nhận diện
|      |      |----- phải chính xác tuyệt đối
|      |      |----- ưu tiên SVG
|      |
|      |----- AUTHENTIC
|      |      |----- ảnh thật thuộc đúng project/property/item
|      |      |----- bắt buộc map đúng ITEM
|      |
|      |----- DEMO
|      |      |----- chỉ để demo/prototype
|      |      |----- không được giả thành dữ liệu thật trên live
|      |
|      |----- EDITORIAL
|      |      |----- ảnh bài viết/nội dung
|      |      |----- có nghĩa nội dung nhưng không nhất thiết thuộc BĐS cụ thể
|      |
|      |----- DECORATIVE
|      |      |----- ảnh trang trí
|      |      |----- không được dùng như bằng chứng dữ liệu thật
|      |
|      |----- PLACEHOLDER
|      |      |----- trạng thái cố ý khi thiếu asset
|      |
|      |----- DATA_VISUAL
|             |----- floorplan / map / progress / sơ đồ dữ liệu
|             |----- phải có owner/data thật
|             |----- CẤM bịa
|
|----- GĐ4. SẢN XUẤT ASSET MASTER CHẤT LƯỢNG CAO
|      |
|      |----- Raster master
|      |      |----- Full HD class tối thiểu
|      |      |----- 4K class ưu tiên
|      |      |----- hero/full-bleed: 4K ưu tiên/bắt buộc theo project policy
|      |
|      |----- Ví dụ theo tỉ lệ
|      |      |----- 16:9: 1920×1080 min / 3840×2160 preferred
|      |      |----- 1:1: 1920×1920 min / 3840×3840 preferred
|      |      |----- 9:16: 1080×1920 min / 2160×3840 preferred
|      |
|      |----- CẤM
|      |      |----- lấy ảnh nhỏ kéo to rồi gọi là 4K thật
|      |      |----- chắp vá ảnh nhỏ/mờ
|      |      |----- watermark lạ
|      |      |----- text rác từ AI
|      |      |----- ảnh không rõ identity rồi gán cho item thật
|      |      |----- Claude tự tìm/generate/substitute ảnh
|      |
|      |----- Nếu final UI visible 8 ảnh unique
|             |----- pack phải tồn tại đủ 8 mapping
|             |----- không được render 8 rồi giao 4 để Claude lặp
|
|----- GĐ5. PRODUCTIONIZE ASSET
|      |
|      |----- MASTER SOURCE
|      |      |----- bản lưu trữ/authority chất lượng cao nhất
|      |
|      |----- WEB DELIVERY
|      |      |----- file thực tế Claude dùng trên web
|      |      |----- sắc nét nhưng tối ưu dung lượng hợp lý
|      |
|      |----- Responsive art direction
|      |      |----- nếu cùng master crop ổn desktop/mobile
|      |      |      |----- 1 delivery + objectPosition theo breakpoint
|      |      |----- nếu bố cục đổi mạnh / crop phá chủ thể
|      |             |----- desktop delivery + mobile delivery riêng
|      |
|      |----- Mỗi asset cần
|             |----- FILE / ID
|             |----- ITEM
|             |----- ROUTE / SECTION / ROLE
|             |----- CLASSIFICATION
|             |----- MASTER dimensions/format/checksum
|             |----- DELIVERY dimensions/format/weight
|             |----- ALLOWED_USAGE
|             |----- ratio theo usage
|             |----- objectPosition theo usage/breakpoint
|             |----- SAFE_AREA nếu có
|             |----- transparency / dominant color nếu hữu ích
|             |----- destination path để Claude lưu vào project
|
|----- GĐ6. ASSET QA + DRIVE FREEZE
|      |
|      |----- QA kỹ thuật
|      |      |----- native/high-res thật?
|      |      |----- dimensions đúng?
|      |      |----- format đúng?
|      |      |----- checksum đúng?
|      |      |----- không duplicate sai?
|      |
|      |----- QA thẩm mỹ
|      |      |----- sắc nét?
|      |      |----- không méo/noise/watermark/text rác?
|      |      |----- đúng tone/brand?
|      |      |----- crop desktop/mobile giữ chủ thể?
|      |
|      |----- QA identity
|      |      |----- ảnh thuộc đúng ITEM?
|      |      |----- AUTHENTIC/DATA_VISUAL có owner đúng?
|      |      |----- DEMO không giả live data?
|      |
|      |----- Đẩy vào MỘT folder Google Drive của project
|      |      |----- 01_MASTER_ASSETS
|      |      |----- 02_WEB_DELIVERY
|      |      |----- 03_BRAND
|      |      |----- 04_PROJECTS
|      |      |----- 05_RENTALS
|      |      |----- 06_EDITORIAL
|      |      |----- 07_DATA_VISUAL
|      |      |----- 08_PLACEHOLDERS
|      |      |----- 09_MANIFEST
|      |      |----- 10_FINAL_UI_REFERENCE
|      |
|      |----- Xác nhận Claude truy cập/tải được
|      |----- Git không phải kho dump tất cả master 4K
|
|----- GĐ7. DỰNG UI REFERENCE DETERMINISTIC
|      |
|      |----- Image generation dùng để tạo asset thành phần khi phù hợp
|      |----- Final page KHÔNG được là một ảnh AI tự bịa geometry
|      |
|      |----- Dùng chính frozen production asset pack
|      |----- Dùng chính font/content/constraint thật khi có
|      |
|      |----- Spec khai báo trước
|      |      |----- container
|      |      |----- columns
|      |      |----- gaps
|      |      |----- section paddings
|      |      |----- semantic aspect ratios
|      |      |----- typography sizes/weights/line heights
|      |      |----- breakpoints
|      |      |----- crop/objectPosition
|      |
|      |----- SPEC → COMPOSITION → RASTER
|      |
|      |----- CẤM
|             |----- RASTER → CLAUDE ĐO PIXEL → MAGIC NUMBER
|
|----- GĐ8. RESPONSIVE / CONTENT / STATE / MOTION DESIGN
|      |
|      |----- Responsive
|      |      |----- dùng breakpoint thật của project
|      |      |----- test/reference tại đúng ranh giới layout quan trọng
|      |      |----- 1920 chỉ thêm khi full-width/full-bleed cần kiểm tra
|      |
|      |----- Content
|      |      |----- ưu tiên text thật, tiếng Việt thật
|      |      |----- dùng cả short + long representative values
|      |      |----- content envelope: maxLines/clamp/noWrap/range
|      |
|      |----- State nếu áp dụng
|      |      |----- NORMAL
|      |      |----- LONG_TEXT
|      |      |----- SHORT_TEXT
|      |      |----- IMAGE_MISSING
|      |      |----- PARTIAL_DATA
|      |      |----- EMPTY
|      |      |----- FEW_ITEMS
|      |      |----- LOADING
|      |      |----- chỉ vẽ riêng khi state làm đổi bố cục
|      |
|      |----- Motion
|             |----- ChatGPT là Motion Authority
|             |----- trigger
|             |----- duration
|             |----- easing
|             |----- distance
|             |----- stagger
|             |----- orchestration/order
|             |----- never-animate
|             |----- reduced-motion
|
|----- GĐ9. USER VISUAL APPROVAL
|      |
|      |----- User xem final UI reference
|      |
|      |----- Nếu chưa thích
|      |      |----- ChatGPT sửa design/asset/spec
|      |      |----- Claude CHƯA tham gia
|      |
|      |----- Nếu thích
|             |----- VISUAL_DIRECTION_APPROVED
|             |----- vẫn CHƯA đồng nghĩa implementation-ready
|
|----- GĐ10. IMPLEMENTATION READY GATE
|      |
|      |----- user visual approved? YES/NO
|      |----- asset count plan đã báo? YES/NO
|      |----- asset visible đủ 100%? YES/NO
|      |----- FHD/4K-class master đạt chuẩn? YES/NO
|      |----- web delivery đủ? YES/NO
|      |----- Drive upload + accessible? YES/NO
|      |----- ITEM/usage mapping đủ? YES/NO
|      |----- full-width/boxed/mixed locked? YES/NO
|      |----- typography locked? YES/NO
|      |----- semantic geometry locked? YES/NO
|      |----- responsive locked? YES/NO
|      |----- required states locked? YES/NO
|      |----- motion locked or N/A? YES/NO
|      |----- no unresolved asset/spec blocker? YES/NO
|      |
|      |----- Có ít nhất 1 NO
|      |      |----- IMPLEMENTATION_READY_UI = false
|      |      |----- KHÔNG giao Claude
|      |
|      |----- Tất cả applicable = YES
|             |----- IMPLEMENTATION_READY_UI = true
|             |----- mới tạo Claude task
|
|----- GĐ11. CHATGPT TẠO CONTRACT NGẮN CHO CLAUDE
|      |
|      |----- ROUTE
|      |----- SECTION
|      |----- FILES nếu biết
|      |----- SCOPE: LOCAL / SHARED
|      |----- CURRENT
|      |----- TARGET
|      |----- ASSET SOURCE / exact mapping
|      |----- LAYOUT / TYPOGRAPHY / RESPONSIVE
|      |----- MOTION / INTERACTION nếu có
|      |----- DO NOT CHANGE
|      |----- ACCEPTANCE
|      |
|      |----- Không nhét lại cả skill 500 dòng vào task
|      |----- Không bắt Claude nghiên cứu lại toàn project
|
|----- GĐ12. CLAUDE IMPLEMENTATION
|      |
|      |----- Không planning dài
|      |----- Không audit toàn repo
|      |----- Không external design research
|      |
|      |----- Pre-flight vài giây
|      |      |----- DRIFT CHECK
|      |      |----- SCOPE CHECK
|      |      |----- TOKEN CHECK
|      |
|      |----- Default
|      |      |----- đọc 1–3 file liên quan
|      |      |----- tải đúng delivery asset từ Drive
|      |      |----- lưu đúng destination path
|      |      |----- code đúng contract
|      |      |----- chèn đúng asset
|      |
|      |----- CẤM Claude
|      |      |----- tự search/generate/substitute asset
|      |      |----- map ảnh theo index khi có identity mapping
|      |      |----- tự chế icon/state/motion
|      |      |----- tự đổi full-width/boxed/breakpoint
|      |      |----- đo raster để lấy px/ratio
|      |      |----- mở rộng scope im lặng
|      |
|      |----- Nếu thiếu
|             |----- NEED_ASSET
|             |----- BLOCKED_SPEC
|             |----- TECHNICAL_CONSTRAINT
|             |----- tiếp tục phần không bị ảnh hưởng nếu an toàn
|
|----- GĐ13. TECHNICAL CHECK TỐI THIỂU
|      |
|      |----- check tỷ lệ với scope
|      |      |----- typecheck/lint/build khi phù hợp
|      |      |----- responsive mới → smoke browser nhanh nếu cần
|      |      |----- interaction phức tạp → targeted interaction test
|      |      |----- backend/security/data → targeted tests
|      |
|      |----- KHÔNG mặc định screenshot matrix
|      |----- KHÔNG mặc định full test suite cho thay đổi UI tĩnh nhỏ
|      |
|      |----- Claude báo 3–5 dòng
|             |----- Changed
|             |----- Checks
|             |----- Assets matched/missing
|             |----- Blocked
|             |----- HEAD nếu có
|
|----- GĐ14. USER ACCEPTANCE TRÊN WEB THẬT
|      |
|      |----- User là người nghiệm thu visual cuối
|      |----- xem desktop/mobile/wide nếu cần
|      |----- xem full-width/container/crop/font/spacing/motion/interaction
|      |
|      |----- Nếu chưa đạt
|      |      |----- DESIGN ERROR → ChatGPT sửa spec/design
|      |      |----- ASSET ERROR → ChatGPT sửa/tạo asset
|      |      |----- IMPLEMENTATION ERROR → Claude sửa code theo contract
|      |
|      |----- Nếu đạt
|             |----- USER_APPROVED
|
|----- GĐ15. FUNCTIONAL QA
|      |
|      |----- chỉ sau khi UI đã đạt hoặc user yêu cầu sớm hơn
|      |----- kiểm tra chức năng thật
|      |----- customer side / admin side / data paths
|      |----- tạo BUG ID ổn định
|      |----- không dùng QA để redesign UI
|
|----- GĐ16. BUG FIX
|      |
|      |----- Claude chỉ sửa BUG ID được giao
|      |----- không audit lại cả repo
|      |----- không redesign
|      |----- không external research lại
|
|----- GĐ17. FINAL HANDOFF
       |
       |----- GitHub
       |      |----- source code / branch / commit / PR nếu dùng
       |
       |----- Google Drive
       |      |----- master assets
       |      |----- delivery assets
       |      |----- manifest
       |      |----- final UI references
       |
       |----- Vercel nếu dùng
       |      |----- preview/production URL
       |
       |----- USER FINAL APPROVAL
```

## Thuật ngữ cốt lõi

- **Asset**: tài nguyên giao diện như ảnh, logo, icon, sơ đồ. Tác dụng: cung cấp đúng nguyên liệu mà code sẽ hiển thị.
- **Master Source**: file gốc chất lượng cao nhất. Tác dụng: làm nguồn chuẩn để xuất các biến thể web về sau.
- **Web Delivery Asset**: file đã chuẩn bị để website thực sự tải. Tác dụng: giữ hình đẹp nhưng tránh bắt browser tải master quá nặng.
- **Manifest**: file danh mục khai báo asset nào dùng ở đâu. Tác dụng: Claude không phải đoán hay map theo index.
- **Identity Mapping / ITEM mapping**: ánh xạ asset với đúng thực thể, ví dụ `project:a → a-cover.webp`. Tác dụng: ngăn gán nhầm ảnh.
- **Allowed Usage**: ngữ cảnh một asset được phép dùng. Tác dụng: ngăn ảnh của một dự án xuất hiện sai ở dự án khác.
- **Safe Area**: vùng quan trọng của ảnh không được crop mất. Tác dụng: bảo vệ chủ thể khi responsive.
- **Object Position**: vị trí ưu tiên của ảnh bên trong khung crop. Tác dụng: giữ tòa nhà/khuôn mặt/chủ thể đúng chỗ.
- **Deterministic Composition**: bố cục được tạo từ các giá trị đã khai báo, không phải ảnh AI tùy ý. Tác dụng: render và code có cùng công thức.
- **Raster**: ảnh phẳng PNG/JPG của giao diện. Tác dụng: người dùng nhìn/duyệt; không phải nguồn số đo implementation.
- **Semantic Geometry**: kích thước/tỉ lệ có ý nghĩa thiết kế như `4/3`, `gap 24`, `container 1520`. Tác dụng: code dễ hiểu, không có con số ma thuật.
- **Magic Number**: số đo hardcode không rõ lý do, thường sinh từ đo screenshot. Tác hại: khó duy trì và thường là dấu vết reverse-engineering.
- **Breakpoint**: mốc chiều rộng nơi layout đổi. Tác dụng: điều khiển responsive.
- **Responsive**: giao diện thích nghi theo kích thước màn hình.
- **Content Envelope**: giới hạn nội dung component phải chịu được, như số dòng hoặc độ dài. Tác dụng: dữ liệu mới không làm vỡ layout.
- **State**: trạng thái component như loading/empty/missing image. Tác dụng: thiết kế vẫn đúng khi dữ liệu không hoàn hảo.
- **Motion**: hệ chuyển động của UI. Tác dụng: quy định cách phần tử xuất hiện/di chuyển thay vì Claude tự nghĩ.
- **Implementation Contract**: chỉ dẫn ngắn, chính xác cho task code. Tác dụng: Claude thực thi thay vì thiết kế lại.
- **Pre-flight Check**: kiểm tra nhanh trước khi code. Tác dụng: phát hiện drift/shared scope/token không tồn tại trước khi sửa sai.
- **Drift**: local code khác trạng thái remote/contract. Tác dụng của drift check: tránh sửa dựa trên code cũ.
- **Smoke Check**: kiểm tra nhanh website có chạy và không có lỗi lớn. Tác dụng: phát hiện lỗi runtime/layout cơ bản mà không mở vòng QA dài.
- **Implementation Ready Gate**: cổng kiểm tra UI đã đủ nguyên liệu để code. Tác dụng: chặn việc giao Claude quá sớm.
- **Visual Direction Approved**: user đã thích hướng nhìn. Chưa đồng nghĩa đủ nguyên liệu để code.
- **Implementation Ready UI**: UI đã đủ asset/spec/mapping/responsive/state để Claude triển khai mà không cần bịa.
