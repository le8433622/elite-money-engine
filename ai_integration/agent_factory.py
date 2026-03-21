import random
from decimal import Decimal
from core_system.logging import get_logger
from data.models import AutonomousAgent

logger = get_logger("agent_factory")

agent_niches = [
    "Crypto Arbitrage Bot", 
    "High-frequency Options Trader", 
    "Darkpool Liquidity Sniper", 
    "AI SaaS Autobuilder", 
    "DeFi Flashloan Attacker"
]

class AgentFactory:
    def spawn_agent(self, budget: Decimal) -> dict:
        """Nhà máy đẻ ra một thực thể AI Agent tự làm việc kiếm tiền"""
        niche = random.choice(agent_niches)
        aname = f"Agent_X{random.randint(100, 999)}_{niche.split()[0]}"
        logger.info(f"[AGENT FACTORY] Sinh tồn: Đã ấp nở chiến binh {aname} với vốn {budget} USD")
        return {
            "name": aname,
            "niche": niche,
            "capital": budget
        }

    def simulate_agent_business(self, agent: AutonomousAgent) -> Decimal:
        """Agent tự hành động càn quét thiên hà Web để mang siêu lợi nhuận về cho Vua Chúa"""
        if agent.status != "active": 
            return Decimal("0.0")
        
        # Tỷ lệ Lợi Nhuận: Gấp 0.5 đến gấp 5 lần số vốn RẤT ĐIÊN RỒ
        multiplier = Decimal(str(round(random.uniform(0.5, 5.0), 2)))
        roi = agent.capital_allocated * multiplier
        
        logger.info(f"[AUTONOMOUS OS] Tay sai {agent.name} ({agent.niche}) vừa cướp bóc mạng thành công: Mang về ROI khổng lồ {roi} USD.")
        return roi

ai_factory = AgentFactory()
