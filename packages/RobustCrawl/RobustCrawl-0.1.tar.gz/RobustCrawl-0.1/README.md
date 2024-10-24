# RobustCrawl
``` 
playwright install chrome
export OPENAI_API_KEY="yourkey"  
export OPENAI_API_BASE="your base" # optional
```

brew install go

brew install mihomo

set downloaded proxy file in ./config

# Config
save it in ./config/robust_crawl_config.json
```json
{
        "max_concurrent_requests": 500,
        "GPT": {
            "model_type": "gpt-3.5-turbo"
        },
        "TokenBucket": {
            "tokens_per_minute": 20,
            "bucket_capacity": 5,
            "url_specific_tokens": {
                "export.arxiv": {
                    "tokens_per_minute": 19,
                    "bucket_capacity": 1
                }
            }
        },
        "Proxy": {
            "is_enabled": true,
            "core_type": "mihomo", 
            "start_port": 33333,
            "config_paths": [
                "the comparative path to the proxy file, download by clash-verge core"
            ]
        },
        "ContextPool": {
            "num_contexts": 5,
            "work_contexts": 15,
            "have_proxy": true,
            "duplicate_proxies": false,
            "ensure_none_proxies":  true,
            "download_pdf": false,
            "downloads_path": "./output/browser_downloads",
            "preference_path": "./output/broswer_config",
            "context_lifetime": 60,
            "context_cooling_time":1
        }
}
```