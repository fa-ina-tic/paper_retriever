> [!IMPORTANT] LlamaIndex & Langchain은 추상화 정도가 높아 세부적인 customize가 불가능한 경우가 많습니다. 현재 customize한 document parser를 개발 중이고, 이를 통해 문서를 Parsing해야 하는 이 프로젝트에서는 해당 프레임워크들을 고려하지 않겠습니다.

### 목적
---
faiss indexing 중 무엇을 default로 지원하고, 어떤 domain에서 어떤 indexing을 사용할 지 판단합니다.

### 니즈
---
  1. 인덱스의 수정, 추가, 제거의 **성능이 좋아야 합니다**
  2. 검색 속도가 빨라야 합니다.

### 인덱스
---
[reference](https://github.com/facebookresearch/faiss/wiki/Faiss-indexes)

특이사항

`Flat`의 경우 `vector id`를 저장하지 않음(단순 sequential numbering만 사용) -> `id`를 사용한 데이터추가 불가능
