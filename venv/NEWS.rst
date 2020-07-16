v3.1.0 (April 2020)
===================


In this version 3.1.0, we bring a lot of bug fixes, some new nice
features that will help you to use the system more efficiently and
easily. We also enhance some modules so that it works better than
before. See the release note below for more detail:


1. Fixes
--------


1.1. Standard Modules



+ Accounting Posting: fixed accounting posting tool issue about the
  length of the field
+ Batch Upload: fixed error while upload file in Multi Journal
+ Batch Job: fixed when changing System Date it doesn't change the
  date in Batch Job
+ Buy Foreign Currency: fixed error message Inputter and Authorizer
  must be different
+ Collateral Detail: fixed some data input is required when the user
  can leave it blank
+ Collateral: fixed error while creating collateral did not redirect
  to collateral detail while manual ID in collateral detail
+ CBC data upload : fixed unable to download inactive loan
+ Change Loan Product:
    + fixed issue cannot make the change loan product for a loan with AIR
      over hundred
    + fixed wrong provision GL KEYS issue
+ Data Enquiry: fixed while upload file import in "Normal" mode
+ Drawdown Account: fixed error while viewing the drawdown account
  form
+ Expense Posting: fixed error hidden field required while creating a
  new record
+ EOD - End of Day Process :
    + fixed cannot run a batch job error
    + fixed error while sequence did not update correctly
    + fixed schedule addon error while collecting addon "Category not
      found"
    + fixed EOD error while running in the command line
+ Fund Transfer :
    + fixed error while creating auto-generate a record when using
      disburse settlement group loan
    + fixed error while authorizing reversed record
+ Group Loan Collection : fixed cannot create group loan collection
  after saving the record
+ Loan Amendment :
    + fixed error when creating the record with termination operation
    + fixed while creating record amend deduct
    + fixed while amend add principal both loan that has PD and no PD
    + fixed error that is unable to do payment holiday for loan KHR
    + fixed capitalize interest not working
+ Loan Contract:
    + fixed error while disburse loan did not book provision
    + fixed required field in form loan contract
    + fixed FCY/LCY interest income earn
+ Loan Collection: fixed error while doing manual loan collection did
  not collect PD record
+ Loan Recovery: fixed while doing the recovery not able to collect
  all outstanding write off amount rather than PD amount
+ Loan Write Off: fixed while doing the write off with no authorizer
  (self authorized)
+ Loan Center : fixed error while view loan center and UI style
  incorrectly
+ PD: fixed waive PD interest did not update the amount in the
  contract correctly
+ Potential Customer Center : fixed technical error cannot view in
  "Potential Customer Center"
+ Potential Customer: fixed validation on-field "Local Name" and
  "Name" and error in Potential Status "Not a valid choice"
+ Saving Plan Contract:
    + fixed while saving the contract to live and repayment schedule is in
      unauthorized record
    + fixed error when accrued Interest saving plan contract
+ System Health Check: fixed error run check "Trail Balance Pop Up"
  and error while check provision when choosing balance type Dr category
+ Sell Foreign Currency: fixed issue wrong accounting posting when
  reversing record and cannot authorize the record
+ Teller Function: fixed withdrawal by cheque when withdrawing over
  account's balance
+ UI : fixed overflow tab cannot be closed



1.2. Additional Modules



+ Borrowing :
    + fixed when creating drawdown account it creates borrowing account to
      in an unauthorized record
    + fixed error while viewing the dashboard
    + fixed error while creating borrowing account and cannot list live
      record
    + fixed error while creating a borrowing contract
    + fixed bugs while viewing the borrowing schedule
+ Fixed Asset: fixed UI on fixed asset user report and error while
  viewing the asset report
+ LOS Feature : fixed when enabling LOS feature cannot create
  collateral
+ Payment Gateway: fixed error when request account validation
+ Survey: fixed bug when questionnaire has more than one text-area
  fields


2. Features
-----------


2.1. Standard Modules



+ Line Report: system now can view line report sum by balance type
+ Menu Builder : user now able to build menu more easily with drag and
  drop menu to any level that you want. The new menu builder route is:
  /MenuBuilder 

  .. image:: _static/v300-end-users-release-note/v310-2.png
     :scale: 70%

+ Quick Search: user can search for information or data and perform
  the action such as create, authorize the record faster. To search just
  click on the Search bar on the Top Right Corner, the search dialog
  will pop up. 

  .. image:: _static/v300-end-users-release-note/v310-3.png
     :scale: 70%

+ Trial Balance: user able to view Trial Balance by currency



2.2. Additional Modules



+ Account Payable and Receivable (AR/AP)
    + user able to maintain an account in general ledger used to record
      summary purchase transactions
    + user able to do credit invoice sales transactions and the receipt of
      cash from customers


3. Enhancements
---------------

3.1. Standard Modules


+ Report Builder: now report builder has responsive UI
+ Loan Amendment: loan amendment now can collect interest from the
  current installment and the user can use collect and collect and waive
  together.
+ Manual Schedule: schedule now can set flexible interest rate by
  installment


3.2. Additional Modules



+ Fixed Asset

    + add new feature inter-branch to fixed asset
    + user can do backdate create an asset, deposal, transfer,
      repair/maintenance
    + add a feature to depreciate in level asset
    + add discount amount and Auto Fixed Asset Coding



v3.0.0 - beta 2 (Oct 2019)
=========================

There are some bugs fixed on release vb version 3.0.0 according to
this, we released this beta version for fixing any bugs on that
version. We will continue to find more bugs and fix with the next beta
version until our version 3.0.0 will be stable.


1. Fixes
--------


1.1. Standard Modules



+ Account Statement : fixed when view account statement shows
  incorrect calculated In/Out and balance amount
+ Customer :
    + fixed issue when save record customer on "SpoOccupation" field when
      user change "MaritalStatus" to single after edit record
    + fixed unable to create customer with LOS option enabled
    + fixed "Last Name (English)" does not apply validation - English
      character only
+ Collateral Detail : fixed unable to authorize and reverse record
+ Income Posting : fixed fail to select Debit Account


+ Journal Listing Report : fixed column "Transaction", "Category" and
  "GL" always show None
+ Loan Contract :
    + fixed add validation on interest rate of loan product
    + fixed showing "something is not quite right" when choose frequency
      less than 0



1.2. Additional Modules



+ LOS Feature : fixed when enable LOS feature collateral and loan
  application does not show up on first load
+ Borrowing : fixed when create draw down account it create borrowing
  account to in unauthorized record



1.3. System Core



+ System Core:
    + Remove unused code and double function.
    + Fix missing header in API login
    + Fix Wing API
    + Upgrade new user interface to apply license code

.. _Release-note-v3.0.0:


v3.0.0 - beta 1 (March 2019)
============================



Starting from v3.0.0, Morakot Technology will separate our modules
into 3 main categories:


+ Additional Modules: this kind of module is not available in the
  standard package. Client must request for deployment, and setup
  configuration in order to use these modules. *This is considered as
  change request.*
+ Standard Modules: this is the standard modules inside the standard
  package.
+ System Core: this kind of module will focus on system maintenance,
  admin tools, security, and some other changes of Morakot Core
  Framework.



1. New Features
---------------


1.1. Standard Modules



+ Group : new module to manage group of Village Bank.
+ Group Loan : group loan now can be generated faster than before with
  new Group Loan Module.
+ Log User Activity and System Audit Trail : Morakot VB can now track
  user activities on more module such as who run EOD, backup database.
+ Menu Builder : user now can create menu easily than before. With
  menu builder, you can just drag and drop menu item. What you see is
  what you get.
+ Ownership : new module for storing lookup value for field Ownership
  in Loan Contract.
+ Potential Customer : a new customer relationship management system
  (CRM) built right in Morakot VB.
+ Predefined Schedule : a new way to define schedule in advance and
  later can be used to generate schedule quickly by choosing from the
  predefined. *(Group Loan only)*
+ Relation Indicator : now has its own module for storing lookup
  value.
+ Reports : new reports
    + Operations: Loan Collection, Loan Disbursement, Closed Loan
    + NBC report for Bank
+ Support Tools : new support tools
    + Change Loan Product
    + Fix Data Tools
    + GL Mapping Checker
    + Reset Record Lock
    + Accounting Posting
+ Template Base : a new way to create sample repayment schedule
  without having to use schedule define to generate schedule. *(Group Loan only)*



1.2. Additional Modules



+ Borrowing Module : allow MFIs/Bank to manage their loan debts
  similar to our Loan Contract system.
+ Embedding Module : allow user to embed any url into Morakot VB
  system. *(Beta version)*
+ Fixed Asset Management : allow MFIs/Bank to control their fixed
  assets with automated accounting transaction.
+ Loan Origination System (LOS): allows MFIs/Bank operate in more
  efficient way. We streamline the loan approval workflow with the help
  of latest technology.
+ Notification SMS and Email : now Morakot VB has notification through
  SMS and Email.
+ Payment interface: allow third party agents or banks to connect to
  Morakot VB system through payment interface. Currently, WING is fully
  integrated.
+ Survey Module : now MFIs/Bank able to conduct survey with scoring
  report.
+ Schedule Add-on : allow user to apply add-on like Insurance into
  repayment schedule.



1.3. System Core



+ Database Migration : decrease down time restoring database and no
  longer to alter fields and table
+ License Key : License key now will be stored in file instead of
  database
+ Local development for client: client now can develop their own
  modules and batch jobs
+ Open API (Version 1) : Core Framework now supports open API



2. Enhancements
---------------


2.1. Standard Modules



+ Account Statement : change label Account ID to Account Number.
+ Alter Form and Alter Table : now can change label and add validation
  to any fields.
+ Charge : new option to calculate charge based on Loan Balance.
+ Customer : change a few fields type to remote select field and
  remove a few validations.
+ Collateral Detail : change a few fields type to remote select field.
+ Fund Transfer : now support Auto Inter-branch.
+ Group Loan Collection : update User Interface and add Saving
  Collection.
+ Income Statement : able to view report by periods with As of, YTD,
  Current Month, Previous Month and view by select month and year.
+ Loan Amendment :
    + now be able to waive accrue interest of current installment
    + now able to Capitalize Interest as Principal
    + new Future Amendment feature
+ Loan Contract : added new field for NBC reports purpose and change a
  few fields type to remote select field.
+ Loan Application : Change a few fields type to remote select field.
+ Loan Classification (NBC Prakas 344) : we have updated loan contract
  to comply with NBC Prakas 344.
+ Loan Watch Day : able to set waiting day before moving class and
  reset waiting day by period or month-end in loan contract.
+ Loan Prepayment : we have add new option for prepayment penalty
  calculation.
+ Non Individual Customer : allow user be able to create non
  individual customer in customer module.
+ Penalty : added new option to waive or collect PD interest.
+ Provisioning : updated how provisioning works with multi currencies.
+ Repayment Schedule : now it supports payment holiday.
+ Report Builder : able to execute Stored Procedure from the database,
  update report header and can set limit record
+ Teller Functions: able to do fund advance by Officer instead of
  disbursement sheet.
+ Trial Balance : added options to show in trial balance by currency.
+ View Voucher : updated new Custom option.
+ Other
    + Update length of field Note to 100
    + Update field length in some modules


2.2. System Core



+ AutoID: able to add auto ID follow parent auto ID.
+ Multi-select Field: now support multi select field.
+ New access right: accept override (O) : Core Framework now supports
  set access right for user who have permission to accept override.
+ System Health Check : we have updated system health check to version
  2.
+ User Interface : update responsiveness of web application for
  smaller screen such as mobile and tablet.


3. Fixes
--------


3.1. Standard Modules



+ Accounting : fixed account posting when post accounting with income/
  expense in foreign currency.
+ Customer : fixed Khmer name not validate as Unicode and special
  character.
+ Financial Reports : fixed negative movement balance Debit/Credit of
  Trial Balance II.
+ Loan Contract : fixed show loan application ID after authorized and
  reverse record.
+ Loan Center : fixed error when viewing record from History.
+ Loan Recovery : fixed recovery loan contract and show only Principal
  Past Due amount in recovery form.
+ Multi Journal II : fixed error on Multi Journal II which user cannot
  authorize record.
+ Operation Reports : fixed report loan aging by converting foreign
  currency to based currency.
+ Penalty : fixed collecting or waiving penalty.
+ Provisioning : fixed general bugs in Provision booking.
+ Schedule Define : fixed schedule manual ,show debug code on the
  interface.



3.2. System Core



+ System Core : fixed viewing some history record shows data from LIVE
  version instead.
+ Security : fixed security flaw found in our system by security
  company, ENTERSOFT
    + Persistent Cross Site Scripting
    + Authorization Issue
    + Session Hijacking
    + SSL Cookie without Secure Flat Set
    + SSL/ TLS Improper Implementation
    + Improper Logout Implementation
    + No Proper Expiration of a Session


LOS Release Note V3.0.0 (March 2019)
====================================


Loan origination system is start versioning from v3.0.0 in Morakot
Technology framework.


1. Features
-----------

There are features of LOS is listed below :


+ System Admin ( User Management, Branch, Form, Currency , Setting ...)
+ Potential customer
+ Customer Management
+ Collateral
+ Loan Application
+ Loan Contract
+ Workflow
+ Account ( Draw down account , saving ... )
+ Accounting management
+ Credit Scoring
+ Credit Summary
+ API for mobile development


v2.1.2 (February 2020)
======================


1. What's Fixed?
----------------

Here are what's fixed in this version:


+ Loan Origination System(LOS) : fixed cannot enable and disable
  `#4322`_
+ Collateral : fixed collateral does not redirect to collateral detail
  `#4323`_
+ Report : fixed CO performance report `#3959`_


.. _`#4323`: https://support.morakot.it/issues/4323
.. _`#4322`: https://support.morakot.it/issues/4322
.. _`#3959`: https://support.morakot.it/issues/3959



v2.1.1 (January 2020)
=====================


1. What's Fixed?
----------------

Here are what's fixed in this version:


+ Psycopg2 : fixed database library version not support
+ CBC Upload Report : fixed system can get data of report CBC Data
  Upload without lost data at the end month
+ Standing Order : fixed terminate prematurely get amount from field
  Amount
+ License code : Improvement security check license code
+ Line Report : fixed cannot edit line number and add accept override
  message
+ Loan Restructure : fixed error when eod with loan restructure normal
  class
+ UI : fixed UI system overlap tab


v2.1.0 (August 2019)
====================


1. What's New?
--------------

Here are what's new in Morakot VB system:


+ Database migration : decrease down time restoring database and no
  longer to alter fields and table
+ Branch productivity : show data on any branch by configuration


2. What's updated?



+ Arrears Report : can show guarantor in Khmer name



3. What's Fixed?


Here are what's fixed in this version:


+ Provisioning : Loan not book to provision and add FYC Amount
+ Penalty : Fix waive,collect penalty and interest with status GRA
  error
+ CBC Data Upload : System does not validate spouse ID when it Stored
  in database as empty string
+ Report : Fix daily loan collect report
+ Fund Transfer : Fix fund transfer cannot reverse
+ Fix IRR : Fix when authorize loan amendment IRR is wrong and IRR
  change with no message
+ Wing integration : Journal entries did not show TXN ID in user
  reference column
+ Loan Contract : Fix when view record not show loan application ID
  and set visible on field Loan Status
+ Loan Amendment : Fix double deduct amount and removed schedule from
  INAU delete record


v2.0.9 (September 2018)
=======================

1. What's New?
--------------

Here are what's new in Morakot VB system:


+ Relation Indicator
    + Add Relation Indicators Module to System, Allow system administrator
      add by them self.
    + Update forms such as Loan Application, Loan Contract that have field
      Relation Indicator to lookup from table.


2. What's Updated?
------------------

Here are what's updated in Morakot VB system:


+ Collateral
    + Remove validate length from Description on Collateral Detail.
    + Increment more length of field Description.
+ Loan Application
    + Add more value in status field such as Close, Reject.
+ Menu Theme
    + Change from color selection to preset theme easy for user to use
    + Changing menu theme can be done in User or Profile by clicking on
      profile picture.

+ Penalty and Interest Waive
    + Option to waive current interest in Loan Amendment.
    + Option to waive current interest in Penalty waive.


3. What's Fixed?
----------------

Here are what's fixed in Morakot VB system:


+ Adjustment tool
    + Fix multi posting accounting at the same time
+ Alter Form
    + Fix showing extend form in Alter Form
+ Document
    + Fix browser error when open PDF in document module



v2.0.8 (July 2018)
==================

1. What's New?
--------------

Here are what's new in Morakot VB system:


+ System User Interface

    + Allow user to change background color and menu font color in
      Navigation Panel. To set color, go to User Management. 

      .. image:: _static/v200-end-users-release-note/v208-1.png

    + Make scrollbar in Navigation Panel bigger than before


2. What's Updated?
------------------

Here are what's updated in Morakot VB system:


+ Loan Write Off
    + Remove fields TotalRecoveryAmount and RecoveryDate


3. What's Fixed?
----------------

Here are what's fixed in Morakot VB system:


+ Accounting
    + Fix when view voucher, to display correct order of Dr/ Cr instead of
      Cr/ Dr.
+ Loan Write Off
    + Fix error when authorize loan write off
+ NBC Reports
    + Fix nbc report (for line report only): Sub-total is not sum
+ Standard Reports
    + Fix error in report Loan Cash Flow when click to view report
    + Loan Provisioning Report: change formula
      ``ProvisionPerc=getProvisionPerc(ID,AssetClass,MoreThanOneYear)``
    + Potential Customer Detail Listing and Potential Customer Follow Up:
      remove all lines with MarketingOfficer
+ Import/ Export
    + Morakot has disabled import data in Import/ Export to prevent user
      from importing data.
+ System
    + Fix textarea is not hidden when set visible to false



v2.0.7 (November 2018)
======================

1. What's New?
--------------

Here are what's new in Morakot VB system:


+ New Feature - Loan Day
    + Allow user to create daily loan with everyday collection
    + Able to generate schedule with escape holiday
    + Able to generate schedule with mode Declining, Flat, and Anunity
    + There only Forward and no holiday option
    + TotalNumday can be not equal number of installment
    + Other option the same as Monthly loan
    + Extra: For anunity mode, it will be automatic reduce installment in
      case loan balance is negative. This option is work for all Frequency
      Type (Monthly,Weekly,Daily)
+ New Feature - Loading in comfirm message YES/NO
    + Before authorize or save add loading image in comfirm message to
      prevent duplicate click. If you click duplicate confirm system will be
      error.
    + Remove press key ESC to exit screen
+ New Feature - Standing Order
    + Apply to master branch
    + Amortization amount
    + Terminate standing order
    + Fix amount posting on monthly or daily
    + Allow to edit value date or maturity date
    + Booking future date
+ New Feature - Copy Loan reach Maturity
    + Add script for copy loan reach maturity date to HIST


2. What's updated?
------------------

Here are what's updated in Morakot VB system:


+ CBC
    + Add loading status when clicking on generate data as Excel or CSV
    + Add header column when generate data as excel file
    + Update Monthly report on balance sheet round number
    + Add script for export file csv and excel
    + Fix As Of Date to System Date minus one
    + Fix As Of Date for Data Upload.
+ Loan Classification
    + Force re-classification by changed configuration
+ Loan Reach Maturity
    + Update model in ScheduleAddon
    + Check PastDue in ScheduleAddon if it have Amount, Don't move loan to
      HIST
+ Manual Loan Collection
    + This new update allow user to limit number of installment that they
      want to manual collect PD
    + Add codition in case not allow to set limit if there is not PD
+ NBC Report
    + Fix Monthly report on balance sheet round number
+ Officer
    + Add new field LocalFirstname and LocalLastname in module officer
+ Schedule Define
    + Fix Annunity mode in generate by minus accrue interest charge for
      first installment
    + Fix annunity mode for plus charge
+ Report
    + COPerformance
        + Fix view COPerformance crash showing something is not quite right
          when Loan Contract has no Officer
        + Report will show "N/A-BranchID" in column CO ID and "Unknown" in
          column CO Name for Loan Contract has no Officer
        + Add note for Loan Contract has no Officer
+ Special Journal
    + Remove fields from special journal DrAccount, CrAccount,
      OutstandingAmount, ValueDate, MaturityDate, FrequencyType, Frequency,
      LastRunDate, NextRunDate, AccrPerDay, EarnedAmount
    + Remove option amortize amount of special journal
+ System and Core
    + Add Log detail when system Something is not quite right to show
      error.
    + Add validation to not allow post income summary,current year profit,
      retain earning
    + Add field PrevMonthAmount, PrevYearAmount for adjustment
    + Update process of backup gl balance
    + Add OverDueDay in report "Loan Detail Listing"
    + Validate duplicate loan ID when copy from loan amendment to loan
      maturity
    + Update message for copy loan amendment to loan maturity
    + Move loan contract that reach maturity and loan terminate to loan
      maturity
    + Add message, how to run file
    + Validate existing loan to prevent duplicate
    + Move loan maturity from table loan contract to table loan maturity
    + Copy loan terminate from table laon amendment to table loan maturity
    + Add audit for loan maturity
    + Change system date to Maturity date for Date fied


3. What's Fixed?
----------------

Here are what's fixed in Morakot VB system:


+ Branch

    + Fix branch update effect stored value for monthend process
    + Add validation on form branch

+ CBC

    + Fix some bugs in CBC data upload
    + Fix loan product type CBC
    + Fix error next payment date when the loan did not reach payment
      schedule to the cycle "1".
    + Fix Maturity Date
    + Fix As Of Date to System Date minus one.
    + Fix As Of Date for Credit Bureau Cambodia Data Upload.

+ Exchange Rate

    + Fix Issue refer to update decimal plance of exchange rate, it can
      effect with module multi journal, fund trasfer, teller function for
      validate check total debit/credit amount

+ EOD

    + Fix when run EOD uncomplete but system date change

+ Customer

    + Fix exclude check duplicate IDNumber for IDType: B, F, R
    + For type B: Birth Certificate can have the same number from various
      district, refer to ticket
    + For type F, R: Different family can use the same Family or Residence
      Book to register as customer

+ NBC Report

    + Fix cannot export all NBC reports for MFI caused by error in report
      No. 16
    + Fix when export reports to excel, it only export for branch 'HO'
      only.
    + Fix export NBC reports to excel and show blank data

+ GL Mapping

    + Remove validate check matched with balance type of main GL and sub GL

+ Loan

    + Fix move loans reach maturity date to MKT_LOAN_CONTRACT_HIST
    + Fix loan reached maturity not move pd record to hostory record
    + Fix bug loan contract that cannot be viewed in Loan Centre.

+ Manual Loan Collection

    + Fix manual loan collect when authorize with the same user
    + Fix not able to use this module with limit installment of colleact
      PD in case module not required authorize
    + Filter out PD based on penalty option
    + Fix not update next run date of PD record

+ MultiJournalII

    + Fix MultiJournalII set variable incorrect for new monthend

+ Repayment Schedule

    + Fix CUSTOM charge on repayment schedule

+ Report

    + CO-Performance

        + Fix incorrect number of borrower that don't have loan

    + Schedule Define

        + Fix validate on date when upload repayment schedule

    + Trial Balance

        + Fix view Trial Balance with period previous month


+ Standing Order

    + Fix StandingOrder get category with account category

+ System and Core

    + Fix wrong spelling of khmer translation of eighty
    + Fix monthend process get revenue
    + Fix month end how to get profit when close month
    + Fix month end how to get profit for closing month from consol
      balance
    + Upload document from mobile or tablet



v2.0.6 (November 2018)
======================

1. What's New?
-------------

Here are what's new in Morakot VB system:


+ New Feature - Loan Day

    + Allow user to create daily loan with everyday collection
    + Able to generate schedule with escape holiday
    + Able to generate schedule with mode Declining, Flat, and Anunity
    + There only Forward and no holiday option
    + TotalNumday can be not equal number of installment
    + Other option the same as Monthly loan
    + Extra: For anunity mode, it will be automatic reduce installment in
      case loan balance is negative. This option is work for all Frequency
      Type (Monthly,Weekly,Daily)

+ Loading in comfirm message YES/NO

    + Before authorize or save add loading image in comfirm message to
      prevent duplicate click. If you click duplicate confirm system will be
      error.
    + Remove press key ESC to exit screen

+ Standing Order

    + Apply to master branch
    + Amortization amount
    + Terminate standing order
    + Fix amount posting on monthly or daily
    + Allow to edit value date or maturity date
    + Booking future date


2. What's updated?
-----------------

Here are what's updated in Morakot VB system:


+ CBC

    + Add loading status when clicking on generate data as Excel or CSV.
    + Add header column when generate data as excel file.
    + Update Monthly report on balance sheet round number

+ Loan Classification

    + Force re-classification by changed configuration

+ Manual Loan Collection

    + This new update allow user to limit number of installment that they
      want to manual collect PD

+ Report

    + COPerformance

        + Fix view COPerformance crash showing something is not quite right
          when Loan Contract has no Officer
        + Report will show "N/A-BranchID" in column CO ID and "Unknown" in
          column CO Name for Loan Contract has no Officer
        + Add note for Loan Contract has no Officer


+ Special Journal

    + Remove fields from special journal DrAccount, CrAccount,
      OutstandingAmount, ValueDate, MaturityDate, FrequencyType, Frequency,
      LastRunDate, NextRunDate, AccrPerDay, EarnedAmount
    + Remove option amortize amount of special journal

+ System and Core

    + Add Log detail when system Something is not quite right to show
      error.
    + Add validation to not allow post income summary,current year profit,
      retain earning
    + Add field PrevMonthAmount, PrevYearAmount for adjustment
    + Update process of backup gl balance
    + Add OverDueDay in report "Loan Detail Listing"



3. What's Fixed?
----------------

Here are what's fixed in Morakot VB system:


+ Branch

    + Fix branch update effect stored value for monthend process
    + Add validation on form branch

+ CBC

    + Fix some bugs in CBC data upload
    + Fix loan product type CBC
    + Fix error next payment date when the loan did not reach payment
      schedule to the cycle "1".
    + Fix Maturity Date
    + Fix As Of Date to System Date minus one.
    + Fix As Of Date for Credit Bureau Cambodia Data Upload.

+ Exchange Rate

    + Fix Issue refer to update decimal plance of exchange rate, it can
      effect with module multi journal, fund trasfer, teller function for
      validate check total debit/credit amount

+ Customer

    + Fix exclude check duplicate IDNumber for IDType: B, F, R
    + For type B: Birth Certificate can have the same number from various
      district, refer to ticket
    + For type F, R: Different family can use the same Family or Residence
      Book to register as customer

+ NBC Report

    + Fix cannot export all NBC reports for MFI caused by error in report
      No. 16
    + Fix when export reports to excel, it only export for branch 'HO'
      only.
    + Fix export NBC reports to excel and show blank data

+ GL Mapping

    + Remove validate check matched with balance type of main GL and sub
      GL

+ Loan

    + Fix move loans reach maturity date to MKT_LOAN_CONTRACT_HIST
    + Fix loan reached maturity not move pd record to hostory record
    + Fix bug loan contract that cannot be viewed in Loan Centre.

+ Manual Loan Collection

    + Fix manual loan collect when authorize with the same user
    + Fix not able to use this module with limit installment of colleact
      PD in case module not required authorize
    + Filter out PD based on penalty option

+ MultiJournalII

    + Fix MultiJournalII set variable incorrect for new monthend

+ Repayment Schedule

    + Fix CUSTOM charge on repayment schedule

+ Report

    + CO-Performance

        + Fix incorrect number of borrower that don't have loan

    + Schedule Define

        + Fix validate on date when upload repayment schedule

    + Trial Balance

        + Fix view Trial Balance with period previous month


+ Standing Order

    + Fix StandingOrder get category with account category

+ System and Core

    + Fix wrong spelling of khmer translation of eighty
    + Fix monthend process get revenue
    + Fix month end how to get profit when close month
    + Fix month end how to get profit for closing month from consol
      balance



v2.0.5 (December 2017)
=====================

1. What's updated?
------------------

Here are what's updated in Morakot VB system:
*Currency* Update all rate decimal place from 9 to 16
*Loan Amendment* Add new validate if no PE in repayment order(PD
Parameters), user cannot proceed terminate loan contract.


2. What's Fixed?
----------------

Here are what's fixed in Morakot VB system:


+ Loan Center

    + Fix loan center error when column AccrCurrent for charge has no
      value

+ Reports

    + Consolidated Balance

        + Fix error data table when choosing Show FCY Balance yes

    + CO-Performance

        + Fix get wrong number of borrower
        + Improve performance of report
        + Split column Arrear Amount to PD Principal, PD Interest, PD Penalty


v2.0.4 (December 2017)
======================

1. What's updated?
------------------

Here are what's updated in Morakot VB system:


+ Logo

    + Remove default logo.png file and replace with `README.md`_ file



2. What's Fixed?
----------------

Here are what's fixed in Morakot VB system:


+ Loan Amendment

    + Fix loan contract with regular charge and no accrued option will not
      book charge write off when terminating loan contract

.. _`README.md`: http://readme.md/



v2.0.3 (November 2017)
======================


1. What's updated?
------------------

Here are what's updated in Morakot VB system:


+ Account Rule Detail

    + Allow user to setup account rule with minimum balance to zero.


2. What's Fixed?
----------------

Here are what's fixed in Morakot VB system:


+ Saving Capitalization Rounding

    + Fix label in form create account saving showing undifined Account_SV
    + Fix Interest Capitalization with rounding

+ CBC

    + Fix CBC upload when export active customer, show some inactive
      customer.

+ Loan Amendment

    + Fix when terminate loan contract with charge not accrued, showing
      error category not found.



v2.0.2 (November 2017)
======================

1. What's updated?
------------------

Here are what's updated in Morakot VB system:


+ Account

    + Add new field in account setting for setting category type of
      expense and income

+ Loan center

    + Deduct penalty in GRA period in loan center

+ System and Core

    + Add auto backup option in eod command before EOM (End of Month)


2. What's Fixed?
----------------

Here are what's fixed in Morakot VB system:


+ Manual Loan Collection

    + Fix duplicate collection with manual collection and terminate

+ Past Due

    + Fix missing reference when collecting interest in suspend

+ Report CO Performance

    + Fix co performance report to include loan with manual classification



v2.0.1 (November 2017)
======================


1. What's new?
--------------

Here are what's new in Morakot VB System:


+ Penalty Waive and Collection

    + New standard form for penalty collection
    + We have tracked which user have waived penalty
    + Allow user to set authorization level on penalty collection

+ Past Due

    + New option to vertically collect past due


2. What's updated?
------------------

Here are what's updated in Morakot VB system:


+ Loan Amendment

    + Add reference to interest past due collection
    + Waive accrued current installment

+ Loan Classification

    + Update loan classification manual book provision when collecting
      past due and check condition of penalty collect in GRE and PRE period
    + Add user reference to loan change class


3. What's Fixed?
----------------

Here are what's fixed in Morakot VB system:


+ Loan Classification

    + Fix click un-authorize record not found in loan classification

+ Loan Contract

    + Fix accrued reference number and loan check disburse status
    + Fix record reference when collecting interest

+ Report voucher

    + Fix view voucher to view history record,

+ Loan write off

    + Fix show list loan write off when loan do manual classification to
      loss but has no past due


v2.0.0 (November 2017)
======================


Git: 34315743


1. What's new?
--------------

Here are what's new in Morakot VB System:


+ Data Enquiry: With Wing and TrueMoney template, user do not need to
  DD in drawdown account
+ Fund Transfer: Add confirm message drawdown account that has more
  than one loans
+ Schedule Addon Module:

    + New Module for adding collection to repayment schedule like
      insurance, saving,
    + Auto post accounting when run EOD

+ Manual Loan Collection:

    + Allow to collect past due loans manually
    + You can collect loan before run EOD

+ Manual Loan Classification: Allow to manually change loan class
+ Special Journal: Auto special journal will be removed from module
  Special Journal. This feature will be built into a new dedicated
  module called Standing Order ( Next future release)



2. What's updated?
------------------

Here are what's updated in Morakot VB system:


+ Account

    + Set default Currency to Base Currency in Drawdown Account form
    + View Account Statement can now search by Customer's ID or name

+ Accounting Reports

    + Trail Balance

        + Rounding and unrounding changed from 8 decimal to 9 decimal.
        + Verify Trial Balance can now link to GL
        + If main GL has balance and user have mapped category into main gl,
          it will catch as error

    + Financial report get value by report name and line
    + Update excluded account categories in Income/Expense posting
    + Add new field in account setting for setting category type of
      expense and income

+ Customer & Customer Center

    + Add hyper link to loan center
    + Allow Search by ID or Name
    + Add Customer's Khmer Name & Outstanding Balance
    + Handle Double Entry of Client Upon inputting the customer name, DoB,
      primary ID, the system checks based on Customer Name + ID Number, or
      Customer Name + DoB. If duplicated is found alert the user to use
      existing data. The system shall not allow creating a new record.

+ Dashboard and Notification

    + Update showing notification directly to user
    + Update showing notification by access right
    + Add dashboard unauthorize and notification for main collateral
    + Allow user to sort records by ascending or descending in dashbaord
      unauthorize record
    + Allow user to filter records by branch in dashbaord unauthorize
      record

+ Loan Amendment

    + Update confirm message when principal amount exceeds approved amount
    + Update confirm message when changing loan type (Normal or
      Restructured)
    + Add validation, loan amendment record can't be authorized if no
      repayment schedule

+ Loan Center

    + Add link to past due detail
    + User now can search Loan Contract by customer name
    + Change order of Charge and Interest in loan center
    + Add loan balance in repayment schedule history

+ Loan Contract

    + Add validation before authorize loan when loan contract not yet have
      repayment schedule
    + Add validation to check duplicate charge, minimum charge and maximum
      charge
    + Add new option for loan to accrue by loan outstanding
    + Update ScheduleAddon NextRunDate before authorize record
    + Add validation First Collection Date must be smaller than Value Date
    + Add new table for loan accrued detail for log journal entry of loan
      accrued daily.
    + Change Charge Rate's label fix amount to Fixed Amount

+ Repayment Schedule

    + Add validate charge to allow numeric format only

+ Past Due

    + Update interface layout in Past Due

+ System and Core

    + Update journal and account entry to use Postgres auto ID
    + Allow User Disable/Enable Post Future Date
    + Log out and redirect current logged in user to login page while the
      same account is used to log in by another user


3. What's Fixed?
----------------

Here are what's fixed in Morakot VB System:


+ Account

    + Fix concurrent user request update wrong draw down balance and
      previous balance

+ Account Statement

    + Fix worng format layout in Account Statement
    + Fix account statement with custom search and fix access right

+ Accounting

    + Fix recognizing income when loan reverse AIR (exceed amount in
      schedule)
    + Fix Special Journal auto complete Exchange Rate and LCYAmount in
      Journal Entry
    + Fix loan book provision for restructure loan
    + Fix view voucher when viewing history record

+ CBC

    + Fix CBC upload wrong column data

+ Document

    + Fix error when app setting (file extension) is missing

+ Dashboard and Notification

    + Fix Income-Expense booking page not found
    + Fix missing notification after authroize record reverse
    + Fix missing notification when delete unauthorize record

+ Loan Contract

    + Fix loan contract not update suspend to Yes when choose option in
      Loan Type to Restructured
    + Fix loan restructure collection
    + Fix provision booking for standard loan
    + Fix error validation in charge rate
    + Fix loan collect charge
    + Fix missing booking AIR Journal when loan back date

+ Loan Amendment

    + Fix loan amendment book provision and collect past due when account
      balance is greater than or equal to past due amount
    + Fix loan amendment when select operation terminate with no penalty
      to disable field penalty amount

+ Repayment Schedule

    + Fix loan charge rate in repayment schedule
    + Fix loan annuity with charge with total payment not equal every
      installment
    + Fix error in bwd/fwd key when generate schedule using forward within
      month key

+ Teller Functions

    + Fix Withdrawal by cheques with error required category
    + Fix error message when amount is negative

+ Reports

    + Fix bugs in report CO Performance
    + Fix co performance report for manual loan classification
    + Fix bugs record not found in Cash Transaction Report
    + Fix bugs in NBC reports

+ System and Core

    + Fix error socket when login
    + Fix record still lock after reverse record
    + Fix duplicate authorize record in mktcore


v1.2.0 (July 2017)
==================

Git: 604c927e


What's New?
-----------


#. Potential Customer:

    + Update new potential customer with new flow
    + New inquiry and activity management
    + New dashboard for inquiry overview
    + Create new inquiry will filter assignee based on inputter access
      branch
    + Add action for each activity type
    + Add Override for Mobile duplicate
    + Add Link of each status to Overview Inquiry Dashboard
    + Add Activity button in row of inquiry list so that user can click to
      create activity with specific potential customer
    + Add horizontal scrollbar for listing
    + Update Label name of potential customer
    + Add Validation of English and Khmer field (only Englist or Khmer)
    + Add check black list in potential customer when create customer

#. Check blacklist customer:

    + Change searchbox from inputbox to selectbox
    + Update display layout and highlight on the same info of black list

#. Rejected Module:

    + New module for rejecting Potential Customer, Loan Application ect.

#. Document Module:

    + Document is now a seperate module from Customer
    + New design with document preview, navigation and summary detail
    + Add Created on in list view and preview document
    + Add Fade in and out when restore and delete
    + Change delete message, File Size limit message
    + Add Upload Document button when no file upload message appear
    + Add new app setting for document for default view (list or gird)

#. Loan Calculator:

    + Update interface and add link to loan estimator
    + New Loan Estimator to estimate how much amount can be loaned based
      on income and expense of client

#. Teller function:

    + Add disable LCYAmount and Exchange in Fundtransfer
    + Update validation for checking LCYAmount after submit
    + Add alert when Teller deposit to a drawdown account that has 2 more
      loans also show past due of each loan

#. Cash Deposit

    + Add alert when Teller deposit to a drawdown account that has 2 more
      loans also show past due of each loan.

#. Past Due Detail

    + Add more field information in past due

#. Customer Centre

    + Allow search Customer by ID or Name.

#. GL Balance:

    + Update GL Balance by default if current month doesn't have
      transaction, it will take of current month of the last record

#. CBC module

    + Add new multi check CBC
    + Update sql_script change column Amount in MKT_CBC from string to
      numeric

#. Data Enquiry:

    + Update Data Enquiry module to work with WING and TRUE MONEY template

#. General improvement:

    + Improve user interface. Tab (form's tabs) now will be combined into
      a dropdown list when screen size is small or too many tabs


What's Fixed?
------------


#. Customer:

    + Fix gender will be set automatically based on salutation chosen

#. Journal Entry:

    + Fix check validation amount

#. Line Report:

    + Check validation of line report mapping

#. Security:

    + Fix CRSF security token fail, please login again

#. Loan Contract:

    + Loan Contract search ID will not show history record

#. Loan Amendment:

    + Fix loan amendament detail override msg not to show __None
    + Fix loan amendment detail will not delete check list of loan
      contract

#. Schedule Define:

    + Fix error save manual schedule `ticket`_

#. IRR Repayment Schedule:

    + Fix Total Amount not equal repayment amount per month in IRR
      calculation. It's because of round interest and principal before
      calculate total amount

#. Loan Write Off:

    + Fix Loan write off on move Unearn to Income

#. Teller Function:

    + Fix Deposit By Cheque and alert message accept override INAU

#. NBC Reports

    + Fix convert decimal amount of report NBC N06
    + Fix balance sheet nbc to get balance from LCY amount
    + Fix NBC MFI N05 getting value from BS

#. General bugs fix:

    + Fix double entry with refersh page browser
    + Fix Export file name by datetime
    + Fix user online will update branch on user online dashboard when
      user switch branch


Developer Exclusive
-------------------


#. Report builder:

    + New function getInquiryPercentage and getNextDay

#. Extend module `Wiki1`_

    + Developer now can extend module (except model)
    + Error handling in extend form
    + All extend modules will be written in local folder
    + Exclusive sql_script.sql, urlregister/, tools/, and /templates in
      each projects

#. Dashboard builder

    + Allow dashboard customization by project

#. Notification `Wiki2`_

    + Filter notify by branch
    + Notify exclude own record that was created.
    + Notify who can access the module (Access right)
    + Direct notify to user
    + Dynamic notify work flow
    + User can disable notify by profile.
    + Super Admin notify every module.
    + Allow notification customization by project
    + Notify authroize record only inputter
    + Improve Performance

#. Tools

    + update new table for trancate_table.sql
    + update migration transaction date to last month end
    + New folder script/ to strore scripts for developer used
    + mktsetting: fix extend class function getUrlModule to get default
      module route if Ex not exist
    + Add new command for exit vb login prompt (\q,exit), If user name
      equal exit or \q will be extit from vb console

#. System Health Check

    + Fix validate loan outstanding and drawdown balance using mktmoney to
      format amount
    + Add debug mode for developer

#. General improvements

    + Update `README.md`_ file


Exclusive Features
------------------


#. Fee Charge:

    + Add Regular Fee ( Charge on repayment schdule)
    + Allow to accr daily charge (Regular Fee)

#. Repayment Schedule:

    + Add charge and penalty rate to view repayment schedule
    + Add charge and penalty rate to print repayment schedule


.. _`README.md`: http://readme.md/
.. _`Wiki1`: http://git.morakot.it/root/vb/wikis/Notification
.. _`Wiki2`: http://git.morakot.it/root/vb/wikis/Code-Snippets#28-mkt-form-inheritance
.. _`ticket`: http://support.morakot.it/issues/518



v1.1.2 (June 2017) [17.06]
==========================


Git: 8b4c208f



What's New?
-----------


#. AppSetting:

    + Now has Group, Order and Definition:

        + Group allow app settings to be groups
        + App settings can be ordered
        + App setting now has definition that shows as tooltip for user to
          understand what app setting is for.

    + AppSetting url has changed to '/Morakot/Settings/'

#. NBC report is ready to use for both MFI and NGO:

    + NBC report list has custom filter by branch.
    + Each report are affected by report list filter.
    + Update new app setting for NBC.

#. Cross branch customer allows user to select customer from different
   branch based on whether Customer module is restricted or not
   (MKT_CUSTOMER in table MKT_RESTRICT_BRANCH).

    + Collateral : Any customer from different branch.
    + Account : Any customer from different branch.
    + Loan Application : Any customer from different branch.

        + Collateral : Only collateral in current branch belong to customer.
        + Co-Borrower : Any customer from different branch.
        + Guarantor : Any customer from different branch.

    + Loan Contract : Any customer from different branch.

        + Account : Only Account in current branch belong to customer.
        + Collateral : Only collateral in current branch belong to customer.
        + Co-Borrower : Any customer from different branch.
        + Guarantor : Any customer from different branch.


#. New tooltip (Core) for input box when length of text is longer than
   input box.
#. New Loan Estimator tool: Estimate how much amount one can loan
   (/Morakot/LoanEstimator).
#. Update Loan Calculator tool with new interface.
#. New EOD processes:

    + EOD now will show progress bar of each batchjob
    + Add new app setting: StopEODAfterMonthEnd (specify to stop or
      continue when month-end is on holiday.)
    + After each month-end, there will be auto-backup
    + EOD now request once per second rather than ten per second

#. Allow to check CBC Enquiry automatically in Loan Application.
   Requirements

    + AutoID for FRM_CBC must be config
    + AppSetting AutoCBCAction must be config


What's Fixed?
-------------


#. CBC Inquiry:

    + Change hot field from approved amount to applied amount.
    + Update CBC Inquiry report to allow view report by Inquiry ID

#. Account currency field cannot be edited after it is created.
#. Fix Main GL is not highlight as bold in Trail Balance and GL
   Balance Listing.
#. Fix first installment when generating schedule not escape holiday.
#. Fix Loan Contract allow to be authorized after first collection
   date is already passed.
#. Fix fund transfer by disabling LCYAmount field and update
   validation for LCYAmount and ExchangeRate.
#. Update duplicated customer criterias:

    + Exact duplicate customer: (Name, Gender, and DOB) or ID is the same.
    + Potential Duplicate Customer: (Name and Gender) or (Name and DOB)
      are the same



Developser Exclusive


#. App Register (Core): ability to extend form from standard module.
   New extend class will be stored the same structure as app in folder
   "local".(More info in wiki)
#. mkttool:

    + mktmoney: Update formatMoney function, allow override rounding and
      decimal place (Commit: d84f905f)

#. ScheduleDefine:

    + Fix schedule anunity passing wrong parameters (Commit: 20fd9f1a)
    + Fix bug for loan amendment add new variable (Commit: f0fe6e8e)
    + Move loan calculator and loan estimator to file `loancal.py`_

#. Fix mktcore call function redirectAfterAuthorized twice after a
   record is authorized.


.. _`loancal.py`: http://loancal.py/


v1.1.1 (May 2017) [17.05]
=========================
Git: a741fa16

What's New?
-----------


#. App Setting:

    + Add new AppSetting for Loan (IRR Rate Mode)

        + Mode 1: Defualt mode (PaymentAmount=RoundUp, IRRRate=2 Decimal
          point, TotalRound at last installment)
        + Mode 2: (PaymentAmount=RoundDown, IRRRate=15 Decimal point,
          TotalRound at first installment)


#. Loan Contract:

    + Allow set first collection date on holiday.
    + Add option to be able to upload schedule even when not in migration
      mode:

        + migration mode set to yes will be able to upload schedule set to no
          even upload schedule set to no
        + migration mode set to no but upload schedule set to yes still able
          to upload schedule but unable to input field like total interest,
          maturity..etc.


#. Loan Amendment:

    + Loan Amendment can deduct/add or schdule can take penalty amount.

        + Add new field Penalty Amount in Loan Amendment Module
        + Add new field Penalty Amount in PD Parameter Module


#. Accounting:

    + Add new column GL ID in report Voucher and option to hide or show GL
      ID.

#. System:

    + Allow set auto update GL update after EOD.
    + Update BatchUpload clear mode only clear current branch.


What's Fixed?
-------------

#. CBC:

    + Fix CBC - loan inactive missing co borrower and gurantor because
      before when loan terminate does not move to hist now it does.

#. Loan Contract:

    + Fix when Loan Contract is reversed, it will move loan contract
      related data to History
    + Fix ViewRepayment Schedule, wrong loan value date when amend loan
    + Fix Manual Schedule, choosing PI Manual option now will split column
      in to 2
    + Fix remove holiday validation from FirstCollectionDate in Loan
      Contract Module

#. Loan Amendment:

    + Fix Loan Termination process, when loan is terminated, Loan Balance,
      Loan Outstanding, Accrual Current Installment will be reset to zero.

#. Reports:

    + Fix Consolidate Loan Reports, change sum amount from sum of loan
      balance to outstanding amount

#. NBC Reports:

    + General bugs fix and improvement

#. Data Migration:

    + Fix datamigration script with multi currency.

#. System

    + Fix notification missing in multi journal.
    + EOD: Rename Batchjob AccrPrepaidExpense to SpecialJournal.


New Features
------------


#. New Data Migration Tools (Beta):

    + User will be able to validate data before migrate data to Morakot VB
      System.

#. System:

    + Add tooltip in Dropdown list if text more than 41 characters.
    + Add tooltip to textbox of Principal Amount and Interest Amount in
      Manual Schedule.


Developer Exclusive:
--------------------


#. NBC Reports:

    + Fix NBC Report for NGO:

        + Report 03: fix show wrong number of loan
        + Report 04, 08: fix showing wrong rate
        + Report 05: fix when extract to excel, AmountInRiel is wrong. This
          fix will overwrite correct value to cell (Overwrite over formular of
          NBC template)
        + Report 06: fix showing duplicate and zero approved amount,
          collateral valuation price will be summed if customer have more than
          one collateral
        + Report 08: fix show amount by saving account type
        + Report 10



v1.1.0 (April 2017) [17.04]
===========================


Git: b85fc4e4


What's New?
-----------


#. CBC:

    + Update check duplicate enquiry

#. Loan Contract

    + Update Loan Contract form in migration mode
    + Update Repayment Schedule, when printing add HouseNo and StreetNo

#. Loan Amendment

    + Update loan amendment, add penaly when amend loan contract

#. Officer

    + Add new field Phone2 to Officer Module

#. Accounting

    + Add option to see Current Year in Trail Balance


New Features
------------


#. GLAudit

    + User can review all journal posted by non-system user

#. CTR Report

    + Report for NBC about transaction over 40 million riels.

#. Interbranch Recievable and Payable Account


What's Fixed?
-------------

#. NBC Reports:

    + Update New NBC report for Credit Operator

#. Account

    + Fix hyper link for DrawDown Account in loan center.
    + Fix create draw down account cannot select customer with different
      branch

#. Loan Contract

    + Fix Current Installment Interest (get value directly from
      MKT_LOAN_CONTRACT) in Loan Center
    + Fix showing wrong repayment status in loan center when client fully
      paid, but showing partial paid
    + Fix Current Installment Interest in Loan Center to Interest on
      repayment schedule when collection date equal to bankdate
    + Fix update Loan Contract Maturity Date and Total Interest before
      authorize
    + Fix Remove schedule and check New Maturity Date
    + Fix provision booking for loan contract
    + Fix validation First Collection Date must be bigger than System Bank
      Date in Loan Contract

#. Loan Amendment:

    + Fix collect pre-termination order to first
    + Fix check approve amount in loan amendment

#. Accounting:

    + Fix display month order in GL
    + Fix display rate in Trail Balance
    + Fix Fund Settlement loan exchange rate
    + Fix LCY Amount in GL when doing adjustment
    + Fix display month label in advance option of balances sheet report

#. Teller Functions:

    + Update teller function to post forward month but cannot authorize
      and disable field exchange rate
    + Fix fund settle load exchange rate


Developer Exclusive:
--------------------


#. Report Builder:

    + New report builder function getAccountInfo()

#. tools

    + General bugs fix for `mktaccounting.py`_


.. _`mktaccounting.py`: http://mktaccounting.py/



v1.0.2 (March 2017)
===================


Git: d16a7bd0


What's New?
-----------


#. Customer

    + New fields Potential Customer automatically look up informations of
      potential customer into customer ( See New Features `PotentialCustomer`_)
    + Improve check double customer to alert after save
    + Alert new customer if similar with black-list.

#. Loan Contract

    + Limit Approval

        + Allow define limit approval of loan disburse by user or rule.
        + It's power full can set limit approval any form like Journal Entry,
          Multi-Journal, Fund Transfer, Teller Function.

    + Block Customer

        + Blocked customer not allowed to be added as Co-Borrower or Guarantor

    + Loan Accrue Interest

        + Change accrue interest doesn't multiple accr per day with holiday.

#. Loan Amendment

    + Add new field KeepPrevSchedule, and Note to Loan Amendment
    + Add new label tell more information about loan amendment in
      repayment schedule
    + Add new validation, loan reaches maturity date not allowed to amend,
      but if it has past due, allowed to do loan amendment
    + Add new validation, loan from different branch not allowed to do
      loan amendment
    + Add hyper link in error message (Record ID), click on link will open
      new tab showing relative information
    + Add new validate frequency, allow user to user lower case in
      frequency type when generate schedule manual
    + Add new validation to schedule manual, not allow generate schedule
      on collection date when amend loan
    + Add SubTotal to schedule manual after generate schedule
    + Add new column Balance in loan center
    + Change column name from ValueDate to AmendDate in Loan Amendment
      model
    + Change Value Date label to Amend Date in Loan Amendment form
    + Disable Edit, Reverse option for loan amendment
    + Update Loan Contract Value Date will not update after loan amendment
    + Update Disbursed Amount will not change after loan amendment except
      when user amend loan by adding principal, disbursed amount will change
    + Update select field in schedule define manual, and schedule define
      auto to select 2 field.
    + Update Error and Accept Override Message in loan amendment
    + Update journal posting of loan amendment, add Note (Reason field in
      loan amendment), change Reference-SYS to Loan Contract ID, and add
      Reference-USER equal to Loan Amendment ID

#. Accounting

    + Journal Entry

        + Journal entry can use a special journal ( See New Feature `SpecialJournal`_)
        + New field special journal applies with feature special journal.

    + Month End Closing

        + Update report finance with default un-audit report


#. Teller Function

    + Disable booking back date.
    + Allow create record with forward date but cannot authorize.

#. System Security

    + User session: on user can log in to only one device


New features
------------


#. Arhive Data

    + Allow system admin define rule of archive data.

#. Special Journal

    + A special journal is any accounting journal in the general journal
      that is used to record and post transactions of similar types. In
      other words, it’s a place where similar transactions can be recorded
      and organized, so bookkeepers and accountants can keep track of
      different business activities. Example: accountants was post office
      rental every month with the same chart of account and amount.

#. Document attachment

    + This module can be used for store document of customer.
    + Allow attachment file png, jpg, jpeg, gif, pdf.

#. Potential Customer

    + Capture data of potential customer and activities
    + Report potential customer listing and follow up.

#. Black-list check

    + Check the customer was block in system.


What's Fixed?
-------------


#. NBC Reports:

    + General bugs fix and improvements

#. CBC:

    + CBCEnquiry: improvement performance and bugs fix

#. Reports:

    + Branch Productivity report: general bugs fix

#. Loan Contract

    + Loan Write off with penalty: general bugs fix
    + Fix loan contract and repayment schedule, loan charge, guarantor,
      loan co borrower, loan collateral current version after loan amendment
    + Fix update total interest to equal to sum of interest of previous
      installments smaller than amend date plus sum of interest of new
      generated schedule
    + Fix update installment to loan contract when user generate schedule
      using schedule manual
    + Fix update maturity date, total interest, number of installment
      after authorize loan contract or loan amendment instead of after
      saving record
    + Fix wrong loan amendment validate principal amount when amend loan
      adding principal
    + Fix accept override Disbursed amount exceed approved amount
    + Fix spelling ការ => កាល in Repayment Schedule

#. System

    + Improve interval system notification


Developer Exclusive:
-------------------


#. Core

    + Add new control DateTimeField in mktcore

#. Report Builder:

    + Update function lookup address add House No and Street
    + New function in report builder DLOOKUP – using for lookup static
      value

.. _`PotentialCustomer`: https://wiki.morakot.it/http:/#PotentialCustomer
.. _`SpecialJournal`: https://wiki.morakot.it/http:/#SpecialJournal



v1.0.1 (Jan-Feb 2017)
=====================


Git: 15ade0e7


What's New?
-----------


#. Customer

    + Add new fields for Customer for CBC Enquiry and NBC Report:

        + HouseNo, Stree, and Education Level (Tab Current Address and
          Contact)
        + House Ownership, Number of Membr, and Active Member (Family Details)
        + Employer Name, Employer Province, Employer District, Employer
          Commune and Employer Village (Employment Details)
        + Customer Type (Classification)


#. CBC:

    + CBC Data for upload Release 1.11

        + CBC Data version 1.11 updated Address Code and Field 30, 31, 32, 33
          are required to upload with code.
        + CBC Data for upload have active loan and inactive loan upload.
        + CBC Data upload has to two modes Active and Inactive. Active is for
          normal loan and Inactive is for terminated loan.

    + CBC Enquiry V4 (B2B)

        + Allow user check CBC real time in system Morakot VB.
        + Security apply for proxy access.


#. Loan Contract

    + Annuity skip holiday

        + For repayment annuity mode, there is a setting to skip holiday and
          weekend. You can also adjust total amount of annuity per installment.

    + Loan multi-currency & Currency Revelation

        + Add exchange rate by date
        + Improve currency revelation


#. Loan Amendment

    + New module Loan Amendment Detail can change Guarantor, Collateral
      and Co-Borrower.
    + New option for loan amendment to keep old schedule that installment
      smaller than amend date
    + Loan amendment will no longer change Loan contract value date and
      Disbursed amount
    + Loan amendment can no longer be edited after authorized.
    + Loan Amendment: add new field read only Last Paid Amount and
      Installment Amount for CBC inactive.
    + Loan Amendment: change field Value Date to Amend Date and add new
      field Keep Previous Schedule for keep previous schedule which
      installment smaller than amend date (User may or may not paid for the
      installment yet)
    + Paid-Off Penalty

        + Add new option E: If Client paid-off, client will be penalized 25%
          of the total remaining interest


#. Accounting

    + Month End Closing module

        + Book accounting back date previous month no longer need to adjust
          Profit Current Year & Income Summary just run Month End Closing again.
        + Adjustment Year End Closing.
        + View audited/unaudited Balance Sheet and Income Statement report.

    + Console Balance

        + Add option to Console Balance to show FCY Balance

    + Multi Journal

        + Allow booking suspend for clearing account from income/expense
          posting ( Teller ).

    + Inter-Branch Account Module

        + Improve inter-Branch Account.

    + Update View Voucher Report

        + Allow user to view unauthorized records
        + Update view voucher show account

    + Add option show/hide zero balance line in Line Report

        + Balance Sheet and Income statement reports now have option show/hide
          zero balance


#. Teller Function

    + Teller Function

        + Disable booking back date.
        + Allow create record with forward date but cannot authorize.

    + Foreign Exchange Module

        + Buy foreign currency and Sell foreign currency

    + Fund Transfer

        + Module is separate type of fund transfer

    + New field

        + Exchange rate, LCY Amount, Module : is using with multi-currency


#. Report

    + Daily Loan Collection: Allow user criteria between date with actual
      cash collection principal, interest, penalty and charge. Previously,
      Daily Cash Collection.
    + Branch Productivity: list of branches with productivity
      (Outstanding, #Client, PA amount, PA rate…)
    + Network Performance: Add new column (Village Code), fix report
      network performance by adding filter currency
    + Consolidate Loan Report: Add new Total by Currency
    + Loan Aging: Improve report by add currency field
    + Journal Entry Listing : Allow to view user reference.

#. Dashboard

    + Update dashboard add unauthorized with loan write-off and recovery.
    + Branch productivity will show information of the current branch

#. System Maintenance

    + Add system Offline during EOD and will Online after EOD finish.
    + Update role/right to access running EOD without role super admin.

#. GL Balance Transfer

    + Allow transfer balance from Main GL to Sub GL.

#. Migration Mode

    + Allow user to change Loan Balance, Maturity Date, Total Interest
      when creating new loan contract
    + Allow user to upload self-define schedule to a new created loan
      contract by upload excel file.

#. System Security

    + Apply cross-site protection.
    + Allow user apply SSL self signed certificate.


New Features
------------


#. Prepayment Profit Tax

    + Automatically booking prepayment profit tax every month end closing.

#. Template Builder

    + Now can be used for creating template for printing like contract of
      customer, print receipt .

#. New System Health Check.

    + New widget in dashboard with system health check for Admin user
      only.
    + Provide information about system health.

#. Data Enquiry Module

    + This module offer user a way to import all kind of data to the
      system to create a template to upload back to system like Fund
      Transfer. The template is built with Report Builder.

#. Customization field (Alter Table, and Form)

    + Allow user add new field by UI
    + Allow order by field and hide fieldNew login background:
    + When big holiday is coming like New Year, Christmas, login
      background change accordingly.

#. Account Statement

    + New design interface add column Cash In/Out.
    + Short cut view today transaction.


What's Fixed?
-------------


#. NBC Reports

    + General bugs fix and improvement for NBC reports

#. Loan Amendment

    + When choosing operation Termination no longer show the wrong mode.

#. CBC 8 CBC data upload with the terminated loan only need to upload
   once to CBC so there is a range of date you can select usually for one
   month. Note loan that is terminated before update code will not worked
   correctly. To upload Inactive will need to add it manually to Active
   CSV file.
#. Accounting

    + Fix Trail Balance with rounding amount
    + Fix check access right in month end closing and accounting period
    + Fix permission of accounting report (Balance Sheet, Income
      statement, Trial Balance)

#. Repayment Schedule

    + Fix Schedule Record ID when move to History

#. PastDue

    + Update status of deafult PD Parameter
    + Update formula cal penalty in PD PARAM

#. Loan Contract

    + Fix loan charge and Accr Int on Month End


Developer Exclusive
-------------------


#. Report Builder:

    + Add function lookup address with Khmer, English languages
    + Add function to set custom value: FIXVALUE
    + Update Report builder with grand total with rounding

#. Custom App

    + Development customization new module.

#. Morakot Core

    + Update record lock with add lock record when new record, when user
      logout record lock will be deleted.
    + Fix history record: history record will no longer be edited,
      authorized, or deleted

#. Batch Job

    + Rework on new Batch Job System



v1.0.0 (2015 - 2017)
====================


Standard Morakot VB come with following modules:



#. Customer and standard reports
#. Collateral and standard reports
#. Account and standard reports
#. Loan Application
#. Loan Contract

    + Loan Contract
    + Loan Amendment
    + Standard reports

#. Fund Transfer:

    + Fund Transfer
    + Fund Advance
    + Fund Settlement

#. Teller Functions:

    + Till Open and Close
    + Deposit and Withdrawal
    + Till to Till Transfer
    + Income and Expense Posting
    + Standard reports

#. Accounting:

    + Journal and Multi journal entry
    + View Voucher
    + Income and Expense Booking
    + Standard Accounting Report (Trial Balance, Balance Sheet, and Income
      Statement)

#. NBC Reports version 1.0
#. System Maintenance:

    + EOD
    + Backup and Restore database
    + Data Import/Export
    + Setting

#. Administration Function:

    + User management
    + Menu management
    + Role and right management
    + List of values management (Business, Country, Provice, District,
      Commune, Village, ...)
    + Company profile
    + Branch setup
    + Holiday setup
    + Currency setup
    + Product setup (Loan Product and Account Product)
    + Report Builder
    + Template Builder