from dataclasses import dataclass


@dataclass(kw_only=True)
class TransformersConf:
    # Defined at: transformers.models.auto.auto_factory._BaseAutoModelClass.from_pretrained
    # Link: https://github.com/huggingface/transformers/blob/main/src/transformers/models/auto/auto_factory.py

    pretrained_model_name_or_path: str | None = None

    # Defined at: transformers.generation.configuration_utils.GenerationConfig.__init__
    # Link: https://github.com/huggingface/transformers/blob/main/src/transformers/generation/configuration_utils.py

    # Parameters that control the length of the output
    max_length: int | None = None
    max_new_tokens: int | None = None
    min_length: int | None = None
    min_new_tokens: int | None = None
    early_stopping: bool | str | None = None
    max_time: float | None = None
    stop_strings: list[str] | str | None = None

    # Parameters that control the generation strategy used
    do_sample: bool | None = None
    num_beams: int | None = None
    num_beam_groups: int | None = None
    penalty_alpha: float | None = None
    dola_layers: str | list[int] | None = None

    # Parameters that control the cache
    use_cache: bool | None = None
    cache_implementation: str | None = None
    cache_config: dict | None = None
    return_legacy_cache: bool | None = None

    # Parameters for manipulation of the model output logits
    temperature: float | None = None
    top_k: int | None = None
    top_p: float | None = None
    min_p: float | None = None
    typical_p: float | None = None
    epsilon_cutoff: float | None = None
    eta_cutoff: float | None = None
    diversity_penalty: float | None = None
    repetition_penalty: float | None = None
    encoder_repetition_penalty: float | None = None
    length_penalty: float | None = None
    no_repeat_ngram_size: int | None = None
    bad_words_ids: list[list[int]] | None = None
    force_words_ids: list[list[int]] | None = None
    renormalize_logits: bool | None = None
    constraints: list | None = None
    forced_bos_token_id: int | None = None
    forced_eos_token_id: int | list[int] | None = None
    remove_invalid_values: bool | None = None
    exponential_decay_length_penalty: tuple[int, float] | None = None
    suppress_tokens: list[int] | None = None
    begin_suppress_tokens: list[int] | None = None
    forced_decoder_ids: list[list[int]] | None = None
    sequence_bias: dict[tuple[int], float] | None = None
    token_healing: bool | None = None
    guidance_scale: float | None = None
    low_memory: bool | None = None
    watermarking_config: dict | None = None

    # Parameters that define the output variables of generate
    num_return_sequences: int | None = None
    output_attentions: bool | None = None
    output_hidden_states: bool | None = None
    output_scores: bool | None = None
    output_logits: bool | None = None
    return_dict_in_generate: bool | None = None

    # Special tokens that can be used at generation time
    pad_token_id: int | None = None
    bos_token_id: int | None = None
    eos_token_id: int | list[int] | None = None

    # Generation parameters exclusive to encoder-decoder models
    encoder_no_repeat_ngram_size: int | None = None
    decoder_start_token_id: int | list[int] | None = None

    # Generation parameters exclusive to assistant generation
    is_assistant: bool | None = None
    num_assistant_tokens: int | None = None
    num_assistant_tokens_schedule: str | None = None
    assistant_confidence_threshold: float | None = None
    prompt_lookup_num_tokens: int | None = None
    max_matching_ngram_size: int | None = None
