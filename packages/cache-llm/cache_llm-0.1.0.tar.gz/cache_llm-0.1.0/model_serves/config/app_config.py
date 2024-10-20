from typing import Optional, Dict, Any

class ModelConfig:
    def __init__(self, 
                 model_name: Optional[str] = None,
                 embedding_model_name: Optional[str] = None,
                 api_key: Optional[str] = None,
                 base_url: Optional[str] = None,
                 embedding_api_configs: Optional[Dict[str, Any]] = None,
                 llm_api_configs: Optional[Dict[str, Any]] = None,
                 rerank_api_configs: Optional[Dict[str, Any]] = None,
                 zhipu_api_configs: Optional[Dict[str, Any]] = None,
                 deepseek_api_configs: Optional[Dict[str, Any]] = None):
        self.model_name = model_name
        self.embedding_model_name = embedding_model_name
        self.api_key = api_key
        self.base_url = base_url
        
        self.embedding_api_configs = embedding_api_configs
        self.llm_api_configs = llm_api_configs
        self.rerank_api_configs = rerank_api_configs
        self.zhipu_api_configs = zhipu_api_configs
        self.deepseek_api_configs = deepseek_api_configs

    def update_limit(self, dicts: list, rpm_factor: float, tpm_factor: float):
        for d in dicts:
            d['rpm'] *= rpm_factor
            d['tpm'] *= tpm_factor
        return dicts


if __name__ == "__main__":
    # 使用示例
    embedding_api_configs = {
        # 你的嵌入 API 配置
    }

    llm_api_configs = {
        # 你的 LLM API 配置
    }

    rerank_api_configs = {
        # 你的重排序 API 配置
    }

    zhipu_api_configs = {
        # 你的 Zhipu API 配置
    }

    deepseek_api_configs = {
        # 你的 Deepseek API 配置
    }

    config = ModelConfig(
        model_name="example_model",
        embedding_model_name="example_embedding_model",
        api_key="example_api_key",
        base_url="https://example.com",
        embedding_api_configs=embedding_api_configs,
        llm_api_configs=llm_api_configs,
        rerank_api_configs=rerank_api_configs,
        zhipu_api_configs=zhipu_api_configs,
        deepseek_api_configs=deepseek_api_configs
    )

    print(config.model_name)
    print(config.embedding_api_configs)