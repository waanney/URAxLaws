<div align="center">

<div style="margin: 20px 0;">
  <img src="./assets/logo.png" width="120" height="120" alt="URA-xLaw Logo" style="border-radius: 20px; box-shadow: 0 8px 32px rgba(0, 217, 255, 0.3);">
</div>

# ⚖️ URA-xLaw: Legal Question-Answering for the State Bank of Vietnam

<div align="center">
  <a href="https://github.com/URAx/URA-xLaw"><img src='https://img.shields.io/badge/🔥Project-Page-00d9ff?style=for-the-badge&logo=github&logoColor=white&labelColor=1a1a2e'></a>
  <a href="https://drive.google.com/file/d/1gwgbsQ3AfXQC_IRdWHVUiDGbpamwjYLx/view?usp=sharing"><img src='https://img.shields.io/badge/📄Download-Demo-ff6b6b?style=for-the-badge&logo=google-drive&logoColor=white&labelColor=1a1a2e'></a>
</div>

<div align="center" style="margin: 20px 0;">
  <div style="width: 100%; height: 2px; margin: 20px 0; background: linear-gradient(90deg, transparent, #00d9ff, transparent);"></div>
</div>

</div>

---

##  Giới thiệu

**URA-xLaw** là nền tảng **Chatbot Hỏi – Đáp Văn bản Pháp luật** chuyên biệt cho **Ngân hàng Nhà nước Việt Nam (NHNN)**. Hệ thống được phát triển bởi đội **URAx – Trường Đại học Bách khoa, ĐHQG-HCM**, hướng tới việc **số hóa, minh bạch và tự động hóa** quy trình tra cứu pháp lý trong hệ sinh thái tài chính – ngân hàng.

---

##  Tính năng chính

* **Tra cứu pháp luật chính xác** với **câu trả lời kèm trích dẫn Điều/Khoản**.
* **LawGraph**: Đồ thị tri thức mô hình hóa quan hệ sửa đổi, bãi bỏ, viện dẫn, hiệu lực.
* **LawRAG**: RAG chuyên miền pháp lý tiếng Việt, hỗ trợ **multi-hop retrieval**.
* **AI Multi-Agent** kiểm soát chất lượng đầu ra: Intent, Retriever, Applicability, Guardrail.
* **Diff & Redline**: So sánh phiên bản văn bản để thấy rõ thay đổi.
* **Checklist tuân thủ tự động**: Xuất danh mục hành động kèm căn cứ pháp lý.
* **Change-Watcher Agent**: Tự động cập nhật văn bản mới trong ≤24h.

---

##  Lợi ích

* **Tổ chức tín dụng**: giảm rủi ro vi phạm, tiết kiệm chi phí.
* **Doanh nghiệp/nhà đầu tư**: tiếp cận tri thức pháp luật cập nhật, minh bạch.
* **Cộng đồng học thuật**: hỗ trợ nghiên cứu & giảng dạy pháp luật thực tiễn.
* **Hệ sinh thái tài chính**: đặt nền móng cho **hạ tầng pháp lý số**.

---

##  Kiến trúc & Công nghệ

* **Backend Orchestrator**: FastAPI + Uvicorn.
* **Search & Vector**: Elasticsearch/OpenSearch + Qdrant/Pinecone.
* **LawGraph**: NetworkX/Neo4j.
* **RAG**: Chunk theo Điều/Khoản, hybrid retrieval, multi-hop.
* **Triển khai**: Docker/Compose, Prometheus giám sát.
* **Bảo mật**: RBAC, mã hóa in-transit & at-rest, tuân thủ Nghị định 13/2023.

---

##  Các gói dịch vụ

* **SOLO** – cá nhân/SME cần tra cứu nhanh.
* **TEAM** – nhóm pháp chế/fintech.
* **ENTERPRISE CLOUD** – API, SLA, tích hợp hệ thống.
* **ENTERPRISE SUITE** – triển khai on-prem/private cloud.

---

##  Xem trước Demo tại đây

👉 [Xem demo tại đây](https://drive.google.com/file/d/1gwgbsQ3AfXQC_IRdWHVUiDGbpamwjYLx/view?usp=sharing)

---

##  Đội ngũ phát triển

* **Nguyễn Song Thiên Long** – Trưởng nhóm (AI & Data).
* **Võ Thị Như Quỳnh** – NLP Engineer.
* **Phan Quốc Khoa** – Tư vấn pháp lý & ontology.
* **Lê Ngọc Hùng Dũng** – AI Engineer.
* **Bùi Minh Quân** – AI Engineer.

**Cố vấn chuyên môn**:

* PGS. TS. Quản Thành Thơ – Trưởng Khoa KH\&KT Máy tính, ĐH Bách Khoa HCM.
* ThS. Nguyễn Ngọc Thái – Phó Giám đốc kỹ thuật, Viettel Solutions.

---

##  Giấy phép

URA-xLaw sử dụng dữ liệu pháp luật công khai & hợp pháp theo **Luật Ban hành VBQPPL 2015** và **Luật Tiếp cận Thông tin 2016**. Hệ thống không lưu trữ dữ liệu cá nhân, tuân thủ **Nghị định 13/2023**.

---

<div align="center">
  <div style="width: 100%; max-width: 600px; margin: 20px auto; padding: 20px; background: linear-gradient(135deg, rgba(0, 217, 255, 0.1) 0%, rgba(0, 217, 255, 0.05) 100%); border-radius: 15px; border: 1px solid rgba(0, 217, 255, 0.2);">
    <div style="display: flex; justify-content: center; align-items: center; gap: 15px;">
      <span style="font-size: 24px;">⚖️</span>
      <span style="color: #00d9ff; font-size: 18px;">URA-xLaw – Minh bạch & Chính xác trong pháp lý</span>
      <span style="font-size: 24px;">⚖️</span>
    </div>
  </div>
</div>
