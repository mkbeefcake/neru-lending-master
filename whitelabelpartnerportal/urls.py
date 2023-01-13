from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path
from .decorator import partner_only

from .views import *

app_name = 'whitelabelpartnerportal'
urlpatterns = [
    url('^$', partner_only(login_required(HomeWhiteLabelView.as_view(), login_url='/user/login')),
        name='home-whitelabel'),
    url('whitelabeltraining', partner_only(login_required(WhiteLabelTrainingView.as_view(), login_url='/user/login')),
        name='whitelabeltraining'),
    url('myresiduals', partner_only(login_required(MyResidualsView.as_view(), login_url='/user/login')),
        name='myresiduals'),
    url('enternewleads', partner_only(login_required(EnterNewLeadsView.as_view(), login_url='/user/login')),
        name='enternewleads'),
    url('marketingroi', partner_only(login_required(MarketingRoiView.as_view(), login_url='/user/login')),
        name='marketingroi'),
    path('becomingapartner/edit/<int:pk>', BecomingAPartner_update, name='becomingapartner_edit'),
    path('leadoverview/edit/<int:pk>', lead_update, name='lead_edit'),
    path('salesaffiliates/edit/<int:pk>', affiliate_agent_update, name='affiliate_agent_edit'),
    path('addbankinfo/edit/<int:pk>', bank_info_update, name='paypal_info_update'),
    path('addpaypalinfo/edit/<int:pk>', paypal_info_update, name='bank_info_update'),
    path('create_account', CreateAccountView.as_view(), name='create_account'),
    path('client-created-by-you', ClientCreatedByYouView.as_view(), name='clients-created-by-you'),
    path('addzelleinfo/edit/<int:pk>', zelle_info_update, name='zelle_info_update'),
    url('leadoverview', partner_only(login_required(LeadOverviewView.as_view(), login_url='/user/login')),
        name='leadoverview'),
    url('mysales', partner_only(login_required(MySalesView.as_view(), login_url='/user/login')),
        name='mysales'),
    url('networkmarketing', partner_only(login_required(NetworkMarketingView.as_view(), login_url='/user/login')),
        name='networkmarketing'),
    url(r'becomingapartner$', partner_only(login_required(BecomingAPartnerView.as_view(), login_url='/user/login')),
        name='becomingapartner'),
    url('becomingapartner1$', partner_only(login_required(BecomingAPartnerView1.as_view(), login_url='/user/login')),
        name='becomingapartner1'),
    url('enteraffiliates', partner_only(login_required(EnterAffiliatesView.as_view(), login_url='/user/login')),
        name='enteraffiliates'),
    url('salesaffiliates', partner_only(login_required(SalesAffiliatesView.as_view(), login_url='/user/login')),
        name='salesaffiliates'),
    url('residualsfromaffiliates', partner_only(login_required(ResidualsFromAffiliatesView.as_view(), login_url='/user/login')),
        name='residualsfromaffiliates'),
    url('freesignup', partner_only(login_required(FreeSignupView.as_view(), login_url='/user/login')),
        name='freesignup'),
    url('paidsignup', partner_only(login_required(PaidSignupView.as_view(), login_url='/user/login')),
        name='paidsignup'),
    url('orders', partner_only(login_required(OrdersView.as_view(), login_url='/user/login')),
        name='orders'),
    url('invoices', partner_only(login_required(InvoicesView.as_view(), login_url='/user/login')),
        name='invoices'),
    url('payments', partner_only(login_required(PaymentsView.as_view(), login_url='/user/login')),
        name='payments'),
    url('credits', partner_only(login_required(CreditsView.as_view(), login_url='/user/login')),
        name='credits'),
    url('wholesalepackages', partner_only(login_required(WholesalePackagesView.as_view(), login_url='/user/login')),
        name='wholesalepackages'),
    url('offeringfinancing', partner_only(login_required(OfferingFinancingView.as_view(), login_url='/user/login')),
        name='offeringfinancing'),
    url('whitelabelwebinar', partner_only(login_required(WhiteLabelWebinarView.as_view(), login_url='/user/login')),
        name='whitelabelwebinar'),
    url('buywhitelabelwebsite', partner_only(login_required(BuyWhitelabelWebsiteView.as_view(), login_url='/user/login')),
        name='buywhitelabelwebsite'),
    url('buywhitelabelbusinesspackage',
        partner_only(login_required(BuyWhitelabelBusinessPackageView.as_view(), login_url='/user/login')),
        name='buywhitelabelbusinesspackage'),
    url('viewportals', partner_only(login_required(ViewPortalsView.as_view(), login_url='/user/login')),
        name='viewportals'),
    url('viewwhitelabelwebsite', partner_only(login_required(ViewWhiteLabelWebsiteView.as_view(), login_url='/user/login')),
        name='viewwhitelabelwebsite'),
    url('viewwhitelabelbusinesspackage',
        partner_only(login_required(ViewWhiteLabelBusinessPackageView.as_view(), login_url='/user/login')),
        name='viewwhitelabelbusinesspackage'),
    url('addbankinfo_form', partner_only(login_required(AddBankInfoFormView.as_view(), login_url='/user/login')),
        name='addbankinfo_form'),
    url('addbankinfo', partner_only(login_required(AddBankInfoView.as_view(), login_url='/user/login')),
        name='addbankinfo'),

    url('addpaypalinfo_form', partner_only(login_required(AddPaypalInfoFormView.as_view(), login_url='/user/login')),
        name='addpaypalinfo_form'),
    url('addzelleinfoform', partner_only(login_required(AddZelleInfoFormView.as_view(),
        login_url='/user/login')), name="addzelleinfo_form"),
    url('addpaypalinfo', partner_only(login_required(AddPaypalInfoView.as_view(), login_url='/user/login')),
        name='addpaypalinfo'),
    url('addzelleinfo', partner_only(login_required(addZelleInfoView.as_view(),
        login_url='/user/login')), name='addzelleinfo'),
    
    url('merchant', partner_only(login_required(MerchantView.as_view(), login_url='/user/login')),
        name='merchant'),
    url('fax', login_required(FaxView.as_view(), login_url='/user/login'),
        name='fax'),
    url('tollfree', partner_only(login_required(TollFreeView.as_view(), login_url='/user/login')),
        name='tollfree'),
    url('professionalemail', partner_only(login_required(ProfessionalEmailView.as_view(), login_url='/user/login')),
        name='professionalemail'),
    url('partnercommisssions', partner_only(login_required(PartnerCommissionView.as_view(), login_url='/user/login')),
        name='partnercommisssions'),

    url('productmanagement', partner_only(login_required(ProductManagementView.as_view(), login_url='/user/login')),
        name='productmanagement'),

    url('wholesales', partner_only(login_required(WholesaleView.as_view(), login_url='/user/login')),
        name='wholesales'),
    url('^clients_on_wholesale', partner_only(login_required(ClientsOnWholesaleView.as_view(), login_url='/user/login')),
        name='clients-on-wholesale'),
    url('^partner_resources', partner_only(login_required(PartnerResourceView.as_view(), login_url='/user/login')),
        name='partner_resources'),

    path('manageportal', partner_only(login_required(ManageWhitelabel.as_view(), login_url='/user/login')),
        name='manageportal'),
    url('client_progress', partner_only(login_required(ClientProgress.as_view(), login_url='/user/login')),
        name='clientProgress'),

    url('add_client_portal', partner_only(login_required(AddClientPortals.as_view(), login_url='/user/login')),
        name='add_client_portal'),

    url('^edit_wholesaleee$', partner_only(login_required(EditWholesale.as_view(), login_url='/user/login')), name='edit_wholesaleee'),
    url('^edit_softwares$', partner_only(login_required(EditSoftware.as_view(), login_url='/user/login')), name='edit_softwares'),
    url('edit_tradelines', partner_only(login_required(EditTradeline.as_view(), login_url='/user/login')), name='edit_tradelines'),
    url('edit_usersteps', partner_only(login_required(EditUserSteps.as_view(), login_url='/user/login')), name='edit_usersteps'),

]
