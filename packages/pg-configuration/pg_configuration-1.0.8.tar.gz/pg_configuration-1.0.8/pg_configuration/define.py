KEY_CONFIGURATION = "game_config"
KEY_CONFIGURATION_EXCEL_DIR = "excel_dir"
KEY_CONFIGURATION_CFG_DIR = "cfg_dir"
KEY_CONFIGURATION_BIN_DIR = "bin_dir"
KEY_CONFIGURATION_CODE_DIR = "code_dir"
"""
configuration format
====
{
  "game_config": {
    "excel_dir": "excel",
    "cfg_dir": "cfg_data",
    "bin_dir": "cfg_bin",
    "code_dir": {
      "JAVA": "java",
      "PYTHON": "python"
    }
  }
}
"""