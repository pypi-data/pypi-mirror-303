from datetime import datetime
from enum import IntEnum
from tortoise import fields
from x_model.model import Model, TsTrait, DatetimeSecField
from tg_auth.models import UserRefTrait, UserInfoTrait, User as BaseUser, UserStatus


class AdvStatus(IntEnum):
    defActive = 0
    active = 1
    two = 2
    old = 3
    four = 4
    notFound = 9


class OrderStatus(IntEnum):
    zero = 0
    one = 1
    two = 2
    three = 3
    done = 4
    fifth = 5
    canceled = 6
    paid_and_canceled = 7
    # COMPLETED, PENDING, TRADING, BUYER_PAYED, DISTRIBUTING, COMPLETED, IN_APPEAL, CANCELLED, CANCELLED_BY_SYSTEM


class ExType(IntEnum):
    p2p = 1
    cex = 2
    main = 3  # p2p+cex
    dex = 4
    futures = 8


class DepType(IntEnum):
    earn = 1
    stake = 2
    beth = 3
    lend = 4


class AssetType(IntEnum):
    spot = 1
    earn = 2
    found = 3


class TradeType(IntEnum):
    BUY = 0
    SELL = 1


class PmType(IntEnum):
    bank = 0
    web_wallet = 1
    cash = 2
    gift_card = 3
    credit_card = 4


class TaskType(IntEnum):
    invite_approve = 1


class ExAction(IntEnum):
    """Public"""

    all_curs_taker = 1  # список поддерживаемых валют
    all_coins = 2  # список торгуемых монет по каждой валюте
    all_pms = 3  # список платежных методов по каждой валюте
    all_ads = 4  # список объяв по (buy/sell, cur, coin, pm)
    """ My PMs """
    fiats = 5  # список реквизитов моих платежных методов (fiats)
    fiat_new = 6  # создание моего fiat
    fiat_upd = 7  # редактирование моего fiat
    fiat_del = 8  # удаление моего fiat
    """ Ads """
    my_ads = 9  # список моих ad
    ad_new = 10  # создание ad: (buy/sell, cur, coin, [pm], price_type, price, details, autoreply)
    ad_upd = 11  # редактирование моего ad
    ad_del = 12  # удаление моего ad
    ad_on = 13  # включение моего ad
    ad_off = 14  # выключение моего ad
    """ Orders """
    order_approve = 15  # одобрить заявку
    order_reject = 16  # отклонить заявку
    take_ad = 17  # старт сделки (order) по чужому объявлению (ad) тейкером на сумму amount: (ad_id, amount)
    order_cancel = 18  # отмена order-a (только для buy заявок)
    order_paid = 19  # отправка статуса "оплачено" по buy ордеру
    order_payment_confirm = 20  # отправка подтверждения "получено" по sell ордеру
    get_chat = 21  # получение сообщений чата по ордеру
    send_msg = 22  # отправка сообщения в чат по ордеру с приложенным фото
    appeal_start = 23  # открыть апелляцию по ордеру
    appeal_accept = 24  # согласиться с чужой апелляцией
    appeal_cancel = 25  # отмена своей апелляции
    send_appeal_msg = 26  # сообщение по апелляции
    user_block = 27  # блокировать юзера
    user_review_post = 28  # поставить отзыв юзеру
    user_rating = 29  # рейтинг и отзывы юзера
    ws_chat = 30  # подписка на сообщения в чате
    ws_status = 31  # подписка на изменение статуса ордера
    get_orders = 32  # получшение заявок за заданное время, статус, направление, валюта, монета
    get_order = 33  # получшение инфы по конкретной заявке


class Country(Model):
    id = fields.SmallIntField(True)
    code: int | None = fields.IntField(null=True)
    short: str | None = fields.CharField(3, unique=True, null=True)
    name: str | None = fields.CharField(63, unique=True, null=True)
    cur: fields.ForeignKeyRelation["Cur"] = fields.ForeignKeyField("models.Cur", related_name="countries")
    curexs: fields.ManyToManyRelation["Curex"]
    fiats: fields.BackwardFKRelation["Fiat"]

    _icon = "location"


class Cur(Model):
    id = fields.SmallIntField(True)
    ticker: str = fields.CharField(3, unique=True)
    rate: float | None = fields.FloatField(null=True)
    country: str | None = fields.CharField(63, null=True)

    pms: fields.ManyToManyRelation["Pm"] = fields.ManyToManyField("models.Pm", through="pmcur")
    pmcurs: fields.ReverseRelation["Pmcur"]  # no need. use pms
    pairs: fields.ReverseRelation["Pair"]
    countries: fields.ReverseRelation[Country]

    _name = {"ticker"}
    _icon = "currency-yuan"

    class Meta:
        table_description = "Fiat currencies"


class Coin(Model):
    id: int = fields.SmallIntField(True)
    ticker: str = fields.CharField(15, unique=True)
    rate: float | None = fields.FloatField(null=True)
    is_fiat: bool = fields.BooleanField(default=False)
    exs: fields.ManyToManyRelation["Ex"] = fields.ManyToManyField("models.Ex", through="coinex")

    assets: fields.ReverseRelation["Asset"]
    pairs: fields.ReverseRelation["Pair"]
    deps: fields.ReverseRelation["Dep"]
    deps_reward: fields.ReverseRelation["Dep"]
    deps_bonus: fields.ReverseRelation["Dep"]

    _name = {"ticker"}
    _icon = "coin"

    def repr(self):
        return super().repr() + (self.is_fiat and " (fiat)" or "")

    class Meta:
        table_description = "Crypro coins"


class Ex(Model):
    id: int = fields.SmallIntField(True)
    name: str = fields.CharField(31)
    host: str | None = fields.CharField(31, null=True)
    url: str | None = fields.CharField(63, null=True)
    type: ExType = fields.IntEnumField(ExType)
    logo: str = fields.CharField(511, default="")

    pms: fields.ManyToManyRelation["Pm"]
    pmcurs: fields.ManyToManyRelation["Pmcur"] = fields.ManyToManyField("models.Pmcur", through="pmcurex")
    coins: fields.ManyToManyRelation[Coin]

    agents: fields.ReverseRelation["Agent"]
    curexs: fields.ReverseRelation["Curex"]
    pmcurexs: fields.ReverseRelation["Pmcurex"]
    pmexs: fields.ReverseRelation["Pmex"]
    pairs: fields.ReverseRelation["Pair"]
    deps: fields.ReverseRelation["Dep"]
    tests: fields.ReverseRelation["TestEx"]

    _icon = "exchange"

    class Meta:
        table_description = "Exchanges"
        unique_together = (("name", "type"),)


class Curex(Model):
    cur: fields.ForeignKeyRelation[Cur] = fields.ForeignKeyField("models.Cur")
    ex: fields.ForeignKeyRelation[Ex] = fields.ForeignKeyField("models.Ex")
    countries: fields.ManyToManyRelation[Country] = fields.ManyToManyField(
        "models.Country", through="curexcountry", backward_key="curexs"
    )

    _name = {"cur__ticker", "ex__name"}


class Pair(Model, TsTrait):
    id = fields.SmallIntField(True)
    coin: fields.ForeignKeyRelation[Coin] = fields.ForeignKeyField("models.Coin", related_name="pairs")
    cur: fields.ForeignKeyRelation[Cur] = fields.ForeignKeyField("models.Cur", related_name="pairs")
    fee: float = fields.FloatField()
    ex: fields.ForeignKeyRelation[Ex] = fields.ForeignKeyField("models.Ex", related_name="pairs")
    directions: fields.ReverseRelation["Direction"]

    _icon = "circles-relation"
    _name = {"coin__ticker", "cur__ticker"}

    class Meta:
        table_description = "Coin/Currency pairs"
        unique_together = (("coin", "cur", "ex"),)

    def repr(self):
        return f"{self.coin.ticker}/{self.cur.ticker}"


class Direction(Model):
    id = fields.SmallIntField(True)
    pair: fields.ForeignKeyRelation[Pair] = fields.ForeignKeyField("models.Pair", related_name="directions")
    sell: bool = fields.BooleanField()
    total: int = fields.IntField()
    ads: fields.ReverseRelation["Ad"]

    _icon = "direction-sign"
    _name = {"pair__coin__ticker", "pair__cur__ticker", "sell"}

    class Meta:
        table_description = "Trade directions"
        unique_together = (("pair", "sell"),)

    def repr(self):
        return f"{self.pair.coin.ticker}/{self.pair.cur.ticker} {'SELL' if self.sell else 'BUY'}"


class User(BaseUser, UserRefTrait, UserInfoTrait):  # tg user
    chat_status: UserStatus = fields.IntEnumField(UserStatus, default=UserStatus.LEFT)
    in_channel: bool | None = fields.BooleanField(default=False, null=True)

    agents: fields.BackwardFKRelation["Agent"]
    fiats: fields.BackwardFKRelation["Fiat"]
    limits: fields.BackwardFKRelation["Limit"]
    proteges: fields.BackwardFKRelation["User"]
    vpn: fields.BackwardOneToOneRelation["Vpn"]
    invite_requests: fields.BackwardFKRelation["Invite"]
    invite_approvals: fields.BackwardFKRelation["Invite"]
    lends: fields.BackwardFKRelation["Credit"]
    borrows: fields.BackwardFKRelation["Credit"]
    investments: fields.BackwardFKRelation["Investment"]


class Agent(Model, TsTrait):
    id: int
    ex: fields.ForeignKeyRelation[Ex] = fields.ForeignKeyField("models.Ex", related_name="agents")
    # ex_id: int
    auth: dict = fields.JSONField(null=True)
    user: fields.ForeignKeyRelation[User] = fields.ForeignKeyField("models.User", related_name="agents")
    user_id: int
    assets: fields.ReverseRelation["Asset"]
    orders: fields.ReverseRelation["Order"]
    ads: fields.ReverseRelation["Ad"]

    _icon = "spy"
    _name = {"ex__name", "user__username"}

    def repr(self):
        return f"{self.ex.name}-{self.user.username}"

    def balance(self) -> float:
        return sum(asset.free * (asset.coin.rate or 0) for asset in self.assets)

    class Meta:
        table_description = "Agents"
        unique_together = (("ex", "user"),)

    class PydanticMeta:
        computed = ["balance"]

    class PydanticMetaListItem:
        max_recursion = 1
        backward_relations: bool = True
        exclude = ("user",)
        computed = ["balance"]


class Adpm(Model):
    ad: fields.ForeignKeyRelation["Ad"] = fields.ForeignKeyField("models.Ad")
    pm: fields.ForeignKeyRelation["Pm"] = fields.ForeignKeyField("models.Pm")

    # no need repr()
    _name = {"ad__id", "pm__name"}

    class Meta:
        table_description = "P2P Advertisements - Payment methods"


class Ad(Model, TsTrait):
    id: int = fields.BigIntField(True)
    direction: fields.ForeignKeyRelation[Direction] = fields.ForeignKeyField("models.Direction", related_name="ads")
    price: float = fields.FloatField()
    pms: fields.ManyToManyRelation["Pm"] = fields.ManyToManyField("models.Pm", through="adpm")  # only root pms
    maxFiat: float = fields.FloatField()
    minFiat: float = fields.FloatField()
    detail: str = fields.CharField(4095, null=True)
    autoMsg: str = fields.CharField(255, null=True)
    agent: fields.ForeignKeyRelation[Agent] = fields.ForeignKeyField("models.Agent", "ads")
    status: AdvStatus = fields.IntEnumField(AdvStatus)

    orders: fields.ReverseRelation["Order"]

    _icon = "ad"
    _name = {"direction__pair__coin__ticker", "direction__pair__cur__ticker", "direction__sell", "price"}

    def repr(self):
        return f"{TradeType(int(self.direction.sell.name)).name}: {self.price:.3g}"

    class Meta:
        table_description = "P2P Advertisements"


class Pm(Model):
    name: str = fields.CharField(63, unique=True)
    identifier: str | None = fields.CharField(63, unique=True, null=True)
    rank: int | None = fields.SmallIntField(default=0)
    type: PmType | None = fields.IntEnumField(PmType, null=True)
    template: int | None = fields.SmallIntField(null=True)
    logo: str | None = fields.CharField(127, null=True)
    color: str | None = fields.CharField(7, null=True)
    multiAllow: bool | None = fields.BooleanField(null=True)
    riskLevel: int | None = fields.SmallIntField(null=True)
    chatNeed: bool | None = fields.BooleanField(null=True)

    ads: fields.ManyToManyRelation[Ad]
    curs: fields.ManyToManyRelation[Cur]
    exs: fields.ManyToManyRelation[Ex] = fields.ManyToManyField(
        "models.Ex", through="pmex"
    )  # no need. use pmexs[.exid]
    # orders: fields.ReverseRelation["Order"]
    pmcurs: fields.ReverseRelation["Pmcur"]  # no need. use curs
    pmexs: fields.ReverseRelation["Pmex"]

    _icon = "currency"

    class Meta:
        table_description = "Payment methods"


class Pmcur(Model):  # for fiat with no exs tie
    pm: fields.ForeignKeyRelation[Pm] = fields.ForeignKeyField("models.Pm")
    pm_id: int
    cur: fields.ForeignKeyRelation[Cur] = fields.ForeignKeyField("models.Cur")
    cur_id: int

    fiats: fields.ReverseRelation["Fiat"]
    exs: fields.ManyToManyRelation[Ex]

    _name = {"pm__name", "cur__ticker"}

    # _sorts = ['-limits_count']

    def repr(self):
        return f"{self.pm.name}-{self.cur.ticker}"

    # @classmethod
    # def pydListItem(cls, max_recursion: int = 1, backward_relations: bool = False, exclude: tuple[str] = (), include: tuple[str] = (), force: bool = False) -> type[PydanticModel]:
    #     if not cls._pydListItem:
    #         mo = PydanticMeta
    #         mo.max_recursion = 1
    #         mo.exclude_raw_fields = True  # default: True
    #         # mo.backward_relations = False # default: True
    #         cls._pydListItem = pydantic_model_creator(cls, name=cls.__name__ + 'ListItem', meta_override=mo, exclude=('pmcurexs',))
    #     return cls._pydListItem

    # @classmethod
    # def pageQuery(cls, sorts: list[str], limit: int = 1000, offset: int = 0, q: str = None, owner: bool = None, **kwargs) -> QuerySet:
    #     query = super().pageQuery([], limit, offset, q)
    #     if kwargs.pop('only_empty', None):
    #         query = query.exclude(limits__not_isnull=True)
    #     else:
    #         query = query.annotate(limits_count=Count('limits')).order_by('-limits_count')
    #     return query.filter(**kwargs)

    class Meta:
        table_description = "Payment methods - Currencies"
        unique_together = (("pm", "cur"),)

    class PydanticMeta:
        exclude_raw_fields: bool = False


class Pmex(Model):  # existence pm in ex with no cur tie
    pm: fields.ForeignKeyRelation[Pm] = fields.ForeignKeyField("models.Pm", "pmexs")
    pm_id: int
    ex: fields.ForeignKeyRelation[Ex] = fields.ForeignKeyField("models.Ex", "pmexs")
    ex_id: int | None
    exid: int | None = fields.SmallIntField(null=True)

    _name = {"pm__name", "ex__name"}

    def repr(self):
        return f"{self.pm.name}-{self.ex.name}"

    class Meta:
        table_description = "Payment methods - Currencies"
        unique_together = (("ex", "exid"),)


class Pmcurex(Model):  # existence pm in ex for exact cur, with "blocked" flag
    pmcur: fields.ForeignKeyRelation[Pmcur] = fields.ForeignKeyField("models.Pmcur")
    pmcur_id: int
    ex: fields.ForeignKeyRelation[Ex] = fields.ForeignKeyField("models.Ex")
    ex_id: int
    blocked: bool = fields.BooleanField(default=False)

    _name = {"pmcur__pm__name", "pmcur__cur__ticker", "ex__name"}

    def repr(self, caller: type[Model] = None):
        return ("[X] " if self.blocked else "") + super().repr()

    class Meta:
        table_description = "Payment methods - Currencies"


class Fiat(Model):
    pmcur: fields.ForeignKeyRelation[Pmcur] = fields.ForeignKeyField("models.Pmcur")
    pmcur_id: int
    # country: fields.ForeignKeyRelation[Country] = fields.ForeignKeyField("models.Country", related_name="fiats")
    # country_id: int
    detail: str = fields.CharField(127)
    name: str | None = fields.CharField(127, null=True)
    user: fields.ForeignKeyRelation[User] = fields.ForeignKeyField("models.User", "fiats")
    user_id: int
    amount: float | None = fields.FloatField(default=0)
    target: float | None = fields.FloatField(default=None, null=True)

    orders: fields.ReverseRelation["Order"]

    _icon = "cash"
    _name = {"pmcur__pm__name", "pmcur__cur__ticker", "amount"}

    def repr(self):
        return f"{self.id}: {self.pmcur.repr()} ({self.user.username})"

    class Meta:
        table_description = "Currency accounts balance"

    class PydanticMetaListItem:
        max_recursion: int = 2
        backward_relations = False
        exclude = "user", "pmcur__exs"
        # exclude_raw_fields = True


class Limit(Model):
    pmcur: fields.ForeignKeyRelation[Pmcur] = fields.ForeignKeyField("models.Pmcur")
    pmcur_id: int
    amount: int = fields.IntField(null=True)  # '$' if unit >= 0 else 'transactions count'
    unit: int = fields.IntField(default=30)  # positive: $/days, 0: $/transaction, negative: transactions count / days
    level: float | None = fields.IntField(
        default=0, null=True
    )  # 0 - same group, 1 - to parent group, 2 - to grandparent  # only for output trans, on input = None
    income: bool = fields.BooleanField(default=False)
    added_by: fields.ForeignKeyRelation["User"] = fields.ForeignKeyField("models.User", related_name="limits")
    added_by_id: int

    _icon = "frame"
    _name = {"pmcur__pm__name", "pmcur__cur__ticker", "unit", "income", "amount"}

    def repr(self):
        return f"{self.pmcur.repr()}[{'<-' if self.income else '->'}]"

    class Meta:
        table_description = "Currency accounts balance"


class Asset(Model):
    coin: fields.ForeignKeyRelation[Coin] = fields.ForeignKeyField("models.Coin", related_name="assets")
    coin_id: int
    agent: fields.ForeignKeyRelation[Agent] = fields.ForeignKeyField("models.Agent", "assets")
    agent_id: int
    type: AssetType = fields.IntEnumField(AssetType)
    free: float = fields.FloatField()
    freeze: float | None = fields.FloatField(default=0)
    lock: float | None = fields.FloatField(default=0)
    target: float | None = fields.FloatField(default=0, null=True)

    _icon = "currency-bitcoin"
    _name = {"coin__ticker", "free"}

    def repr(self):
        return f"{self.coin.ticker} {self.free:.3g}/{self.freeze:.3g} user:{self.agent.repr()}"

    class Meta:
        table_description = "Coin balance"
        unique_together = (("coin", "agent", "type"),)

    class PydanticMeta:
        exclude_raw_fields: bool = False


class Order(Model, TsTrait):
    id: int = fields.BigIntField(True)
    ad: fields.ForeignKeyRelation[Ad] = fields.ForeignKeyField("models.Ad", related_name="ads")
    ad_id: int
    amount: float = fields.FloatField()
    fiat: fields.ForeignKeyRelation[Fiat] = fields.ForeignKeyField("models.Fiat", related_name="orders", null=True)
    fiat_id: int | None
    # pm: fields.ForeignKeyRelation[Pm] = fields.ForeignKeyField("models.Pm", related_name="orders", null=True)  # why commented: already has in fiat.pmcur.pm
    # pm_id: int | None
    taker: fields.ForeignKeyRelation[Agent] = fields.ForeignKeyField("models.Agent", "orders")
    taker_id: int
    status: OrderStatus = fields.IntEnumField(OrderStatus)
    notify_pay_at: datetime | None = DatetimeSecField(null=True)
    confirm_pay_at: datetime | None = DatetimeSecField(null=True)

    _icon = "file-check"
    _name = {"fiat__pmcur__pm__name", "ad__direction__sell"}

    def repr(self):
        return f"{self.taker.repr()}: {self.amount:.3g} pm:{self.fiat.pmcur.pm.name}/{self.fiat_id} {self.status.name}"

    class Meta:
        table_description = "P2P Orders"


class Dep(Model, TsTrait):
    pid: str = fields.CharField(31)  # product_id
    apr: float = fields.FloatField()
    fee: float | None = fields.FloatField(null=True)
    apr_is_fixed: bool = fields.BooleanField(default=False)
    duration: int | None = fields.SmallIntField(null=True)
    early_redeem: bool | None = fields.BooleanField(null=True)
    type: DepType = fields.IntEnumField(DepType)
    # mb: renewable?
    min_limit: float = fields.FloatField()
    max_limit: float | None = fields.FloatField(null=True)
    is_active: bool = fields.BooleanField(default=True)

    coin: fields.ForeignKeyRelation[Coin] = fields.ForeignKeyField("models.Coin", related_name="deps")
    coin_id: int
    reward_coin: fields.ForeignKeyRelation[Coin] = fields.ForeignKeyField(
        "models.Coin", related_name="deps_reward", null=True
    )
    reward_coin_id: int | None = None
    bonus_coin: fields.ForeignKeyRelation[Coin] = fields.ForeignKeyField(
        "models.Coin", related_name="deps_bonus", null=True
    )
    bonus_coin_id: int | None = None
    ex: fields.ForeignKeyRelation[Ex] = fields.ForeignKeyField("models.Ex", related_name="deps")
    ex_id: int
    investments: fields.ReverseRelation["Investment"]

    _icon = "seeding"
    _name = {"pid"}

    def repr(self, caller: Model.__class__ = None):
        return f'{self.coin.ticker}:{self.apr * 100:.3g}% {f"{self.duration}d" if self.duration and self.duration > 0 else "flex"}'

    class Meta:
        table_description = "Investment products"
        unique_together = (("pid", "type", "ex"),)


class Investment(Model, TsTrait):
    dep: fields.ForeignKeyRelation[Dep] = fields.ForeignKeyField("models.Dep", related_name="investments")
    dep_id: int
    amount: float = fields.FloatField()
    is_active: bool = fields.BooleanField(default=True)
    user: fields.ForeignKeyRelation[User] = fields.ForeignKeyField("models.User", related_name="investments")

    _icon = "trending-up"
    _name = {"dep__pid", "amount"}

    def repr(self):
        return f"{self.amount:.3g} {self.dep.repr()}"

    class Meta:
        table_description = "Investments"


class TestEx(Model):
    ex: fields.ForeignKeyRelation[Ex] = fields.ForeignKeyField("models.Ex", related_name="tests")
    # ex_id: int
    action: ExAction = fields.IntEnumField(ExAction)
    ok: bool | None = fields.BooleanField(default=False, null=True)
    updated_at: datetime | None = DatetimeSecField(auto_now=True)

    _icon = "test-pipe"
    _name = {"ex__name", "action", "ok"}

    def repr(self):
        return f"{self.ex.name} {self.action.name} {self.ok}"

    class Meta:
        table_description = "Test Exs"
        unique_together = (("action", "ex"),)


class Vpn(Model):
    user: fields.OneToOneRelation[User] = fields.OneToOneField("models.User", related_name="vpn")
    user_id: int
    priv: str = fields.CharField(63, unique=True)
    pub: str = fields.CharField(63, unique=True)
    created_at: datetime | None = DatetimeSecField(auto_now_add=True)

    _icon = "vpn"
    _name = {"pub"}

    def repr(self):
        return self.user.username

    class Meta:
        table_description = "VPNs"


class Invite(Model, TsTrait):
    ref: fields.ForeignKeyRelation[User] = fields.ForeignKeyField("models.User", related_name="invite_approvals")
    ref_id: int
    protege: fields.ForeignKeyRelation[User] = fields.ForeignKeyField("models.User", related_name="invite_requests")
    protege_id: int
    approved: str = fields.BooleanField(default=False)  # status

    _icon = "invite"
    _name = {"ref__username", "protege__username", "approved"}

    def repr(self):
        return self.protege.name

    class Meta:
        table_description = "Invites"


class Credit(Model, TsTrait):
    lender: fields.ForeignKeyRelation[User] = fields.ForeignKeyField("models.User", related_name="lends")
    lender_id: int
    borrower: fields.ForeignKeyRelation[User] = fields.ForeignKeyField("models.User", related_name="borrows")
    borrower_id: int
    borrower_priority: bool = fields.BooleanField(default=True)
    amount: int = fields.IntField(default=None)  # 0 - is all remain borrower balance

    _icon = "credit"
    _name = {"lender__username", "borrower__username", "amount"}

    def repr(self):
        return self.borrower.name

    class Meta:
        table_description = "Credits"
