#!/bin/bash

# ====================================================================================================
# 🔐 FERRAMENTA AVANÇADA DE DEFESA FORENSE LINUX: ANÁLISE DE ROOTKITS COM CHKROOTKIT + RKHUNTER + QUARENTENA
# 🔎 VERIFICAÇÃO AUTOMATIZADA | MOVIMENTAÇÃO DE ARQUIVOS SUSPEITOS | LOGS COM HISTÓRICO E ORGANIZAÇÃO TOTAL
# ====================================================================================================
# Desenvolvido por: [Seu Nome]
# Versão: 2.0
# Data: $(date +%Y-%m-%d)
# ====================================================================================================

# Cores ANSI
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
NC='\033[0m' # No Color

# Diretórios
DATA=$(date '+%Y-%m-%d_%H-%M-%S')
BASE_DIR="$HOME/defesa_rootkit"
QUARENTENA="$BASE_DIR/quarentena"
LOGS="$BASE_DIR/logs/$DATA"

mkdir -p "$QUARENTENA" "$LOGS"

# Cabeçalho
function cabecalho() {
  clear
  echo -e "${BLUE}"
  echo "====================================================================================================="
  echo "     🔐 FERRAMENTA AVANÇADA DE SEGURANÇA FORENSE - DETECÇÃO E ISOLAMENTO DE ROOTKITS EM SISTEMAS LINUX"
  echo "      USANDO CHKROOTKIT + RKHUNTER COM ANÁLISE, LOGS, QUARENTENA E INTERFACE INTERATIVA EM SHELL"
  echo "====================================================================================================="
  echo -e "${NC}"
  echo -e "🕒 Iniciado em: ${YELLOW}$(date)${NC}"
  echo -e "📁 Quarentena:  ${YELLOW}$QUARENTENA${NC}"
  echo -e "🧾 Logs salvos em: ${YELLOW}$LOGS${NC}"
  echo ""
}

# Verificação de dependências
function checar_dependencias() {
  echo -e "🔍 ${YELLOW}Verificando dependências...${NC}"
  for cmd in chkrootkit rkhunter; do
    if ! command -v $cmd &> /dev/null; then
      echo -e "❌ ${RED}Erro: '$cmd' não está instalado.${NC} Instale com: sudo apt install $cmd"
      exit 1
    fi
  done
  echo -e "✅ ${GREEN}Todas as dependências estão instaladas.${NC}\n"
}

# Execução do chkrootkit
function rodar_chkrootkit() {
  echo -e "🧪 ${BLUE}Executando chkrootkit...${NC}"
  sudo chkrootkit > "$LOGS/chkrootkit.log"
  INFECTED=$(grep 'INFECTED' "$LOGS/chkrootkit.log" | tee /dev/tty)
  if [ -z "$INFECTED" ]; then
    echo -e "✅ ${GREEN}Nenhuma ameaça detectada pelo chkrootkit.${NC}"
  else
    echo -e "⚠️  ${YELLOW}Ameaças encontradas pelo chkrootkit!${NC}"
  fi
  echo ""
}

# Execução do rkhunter
function rodar_rkhunter() {
  echo -e "🧪 ${BLUE}Executando rkhunter...${NC}"
  sudo rkhunter --update > /dev/null
  sudo rkhunter --propupd -y > /dev/null
  sudo rkhunter --check --sk --rwo > "$LOGS/rkhunter.log"

  grep -i 'Warning:' "$LOGS/rkhunter.log" | tee "$LOGS/rkhunter_alertas.txt"
  echo -e "✅ ${GREEN}Relatório rkhunter gerado.${NC}"
  echo ""
}

# Isolamento de arquivos suspeitos
function isolar_suspeitos() {
  echo -e "📦 ${YELLOW}Analisando arquivos suspeitos...${NC}"
  SUSPEITOS=$(grep -Eo '/[^ ]+' "$LOGS/rkhunter.log" | sort -u)
  MOVIDOS=0

  for arquivo in $SUSPEITOS; do
    if [ -f "$arquivo" ]; then
      echo -e "⚠️  Arquivo suspeito: $arquivo"
      sudo mv "$arquivo" "$QUARENTENA/" 2>/dev/null && echo -e "➡️  ${GREEN}Movido para quarentena.${NC}" && ((MOVIDOS++))
    fi
  done

  if [ "$MOVIDOS" -eq 0 ]; then
    echo -e "✅ ${GREEN}Nenhum arquivo real movido para quarentena.${NC}"
  else
    echo -e "📁 ${YELLOW}$MOVIDOS arquivo(s) suspeito(s) foram movidos para quarentena.${NC}"
  fi
  echo ""
}

# Menu interativo
function menu_principal() {
  while true; do
    cabecalho
    echo "1️⃣  Verificação completa (chkrootkit + rkhunter + quarentena)"
    echo "2️⃣  Apenas chkrootkit"
    echo "3️⃣  Apenas rkhunter + quarentena"
    echo "4️⃣  Sair"
    echo ""
    read -p "👉 Escolha uma opção: " opcao

    case $opcao in
      1)
        rodar_chkrootkit
        rodar_rkhunter
        isolar_suspeitos
        read -p "Pressione ENTER para voltar ao menu..."
        ;;
      2)
        rodar_chkrootkit
        read -p "Pressione ENTER para voltar ao menu..."
        ;;
      3)
        rodar_rkhunter
        isolar_suspeitos
        read -p "Pressione ENTER para voltar ao menu..."
        ;;
      4)
        echo -e "\n👋 ${BLUE}Encerrando a ferramenta. Fique seguro!${NC}"
        exit 0
        ;;
      *)
        echo -e "❌ ${RED}Opção inválida.${NC}"
        sleep 1
        ;;
    esac
  done
}

# Execução principal
checar_dependencias
menu_principal
