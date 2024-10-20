
t_sentence_array=""
t_sentence_pronoun = []
t_sentence_others=[]
tigrina_whes=['ንመን','እንታይ','ኣበይ','በየን','በየናይ','በበይ','ናበይ','ካበይ','nabeyenay','ናበየናይ','ከመይ','ብኸመይ','ብከመይ','መዓስ','መን','ክንደይ','ኣየናይ','ስለምንታይ','ክንደይ ዝኸውን','መበል ክንደይ','ምስ መን']
possess=[
'ናተይ','ናትካ','ናትኪ','ናትኩም','ናትክን','ናቱ','ናታ','ናቶም','ናተን','ናትና','ናታትኩም','ናታትክን','ናታቶም','ናታተን','ናታትና',
'ናዓይ','ናዓኻ','ናዓኺ','ናዓኹም','ናዓኽን','ንዕኡ','ናዓኣ','ንዕኦም','ንዕአን','ናዓና',
'ንዓይ','ንዓኻ','ንዓኺ','ንዓኹም','ንዓኽን','ንዓኣ','ንዓና']
tigrinaWhesDoubles=['ዝኸውን', 'ርሕቐት', 'ምስ']
tigrina_questions=[
'ዶ','ድየ','ዲኻ','ዲኺ','ዲኹም','ዲኽን','ድዩ','ድያ','ድዮም','ድየን','ዲና',
'ዲየ','ድኻ','ድኺ','ድኹም','ድኽን','ዲዩ','ዲያ','ዲዮም','ዲየን','ድና']
tigrina_pronoun=[
'ንስኻ','ንስኺ','ንሱ','ንሳ','ኣነ','ንሶም','ንሰን','ንሳቶም','ንሳተን','ንስኹም','ንስኽን','ንስኻትኩም','ንስኻትክን','ንሕና']

tigrina_sentence_type_order="no"


indications=[
'እቲ','እዚ','እቲኦም','እቶም','እዚኦም','እቲኤን','እተን','እዚኤን','እዘን','እቲኣቶም','እቶም','እቲኣተን','እተን','እዚኣቶም','እዚኦም','እዞም',
'ነቲ','ነቶም','ነተን','ነታ','ነቲኦም','ነቲአን','ነቲኣ','ነቲኣቶም','ነቲኣተን']

tigrina_etiWith_whes=[
'ከለኻ','ከለኺ','ከለኹም','ከለኽን','ከሎ','ከላ','ከለኹ','ከለዉ','ከለዋ','ከለና']
tigrina_with_whes_present=[
'ዘለኻ','ዘለኺ','ዘለኹም','ዘለኽን','ዘሎ','ዘላ','ዘለኹ','ዘለዉ','ዘለዋ','ዘለና']
tigrina_with_whes_past=[
'ዝነበርካ','ዝነበርኪ','ዝነበርኩም','ዝነበርክን','ዝነበረ','ዝነበረት','ዝነበርኩ','ዝነበሩ','ዝነበራ','ዝነበርና']

tigrina_none_verb_to_be=[
'ኢየ','ኢኻ','ኢኺ','ኢኹም','ኢኽን','ኢዩ','ኢያ','ኢዮም','ኢየን','ኢና']
question_verb_additions_on_future=['ት','ክ','ይ','ዝ']

tigrinaNoneVerbToBeNegative=[
'ኣይኮንኩን','ኣይኮንካን','ኣይኮንክን','ኣይኮንኩምን','ኣይኮንክንን','ኣይኮነን','ኣይኮንክን','ኣይኮኑን','ኣይኮናን','ኣይኮንናን']
tigrina_past_verb_to_be=[
'ኔረ','ኔርካ','ኔርኪ','ኔርኩም','ኔርክን','ኔሩ','ኔራ','ኔሮም','ኔረን','ኔርና',
'ነረ','ነርካ','ነርኪ','ነርኩም','ነርክን','ነሩ','ነራ','ነሮም','ነረን','ነርና',
'ነይረ','ነይርካ','ነይርኪ','ነይርኩም','ነይርክን','ነይሩ','ነይራ','ነይሮም','ነይረን','ነይርና']
tigrina_verb_to_be_history=['ነበርኩ','ነበርካ','ነበርኪ','ነበርኩም','ነበርክን','ነበረ','ነበረት','ነበሩ','ነበራ','ነበርና']
tigrina_verb_to_be_xenhe=['ጸኒሐ','ጸኒሕካ','ጸኒሕኪ','ጸኒሕኩም','ጸኒሕክን','ጸኒሑ','ጸኒሓ','ጸኒሖም','ጸኒሐን','ጸኒሕና']
tigrina_verb_to_be_xenhe_negative=['ኣይጸናሕኩን','ኣይጸናሕካን','ኣይጸናሕክን','ኣይጸናሕኩምን','ኣይጸናሕክንን','ኣይጸንሐን','ኣይጸነሐትን','ኣይጸንሑን','ኣይጸንሓን','ኣይጸናሕናን']
tigrina_past_verb_to_be_negative=[
'ኣይነበርኩን','ኣይነበርካን','ኣይነበርክን', 'ኣይነበርኩምን','ኣይነበርክን','ኣይነበረን','ኣይነበረትን','ኣይነበሩን','ኣይነበራን','ኣይነበርናን']


tigrina_modal_will_have=['ክህልወካ', 'ክህልወኒ', 'ክህልዎ', 'ክህልዋ', 'ክህልወኪ', 'ክህልወኩም', 'ክህልወክን', 'ክህልዎም', 'ክህልወን', 'ክህልወና']

tigrina_modal_will_not_have=['ኣይክህልወካን', 'ኣይክህልወኒን', 'ኣይክህልዎን', 'ኣይክህልዋን', 'ኣይክህልወኪን', 'ኣይክህልወኩምን', 'ኣይክህልወክንን', 'ኣይክህልዎምን', 'ኣይክህልወንን', 'ኣይክህልወናን']


tigrina_modal_verb_to_be=[
'ኣለኒ','ኣለካ','ኣለኪ','ኣለኩም','ኣለክን','ኣለዎ','ኣለዋ','ኣለዎም','ኣለወን','ኣለና',
'ኣሎኒ','ኣሎካ','ኣሎኪ','ኣሎኩም','ኣሎክን','ኣሎዎ','ኣሎዋ','ኣሎዎም','ኣሎወን','ኣሎና'
,'ኣሎኒ']


tigrina_modal_verb_to_be_negative=[
'የብለይን','የብልካን','የብልክን','የብልኩምን','የብልክንን','የብሉን','የብላን','የብሎምን','የብለንን','የብልናን']


tigrina_have2=[
'ኣለዉኒ','ኣለውኒ','ኣለዉኻ','ኣለውኻ','ስለዉኺ','ኣለውኺ','ኣለዉኹም','ኣለውኹም','ለዉኽን','ኣለውኽን','ኣለዉዎ','ኣለውዎ','ኣለዉዋ','ኣለውዋ','ኣለዉዎም','ኣለውዎም','ኣለዉወን','ኣለውወን','ኣለዉና','ኣለውና']
tigrina_have2_past=['nieromuni','nieromka','nieromuki','nieromukum','nieromukn','nieromo','nieroma','nieromom','nieromen','nieromuna',
'ኔሮሙኒ','ኔሮምኒ','ኔሮሙኻ','ኔሮምኻ','ኔሮሙኺ','ኔሮምኺ','ኔሮሙኹም','ኔሮምኹም','ኔሮሙኽን','ኔሮምኽን','ኔሮሞ','ኔሮማ','ኔሮሞም','ኔሮመን','ኔሮሙና','ኔሮምና']


tigrina_modal_pastVerb_to_be_negative=[
'ኔርኒ','ኔርካ','ኔርኪ','ኔርኩም','ኔርክን','ኔርዎ','ኔርዋ','ኔርዎም','ኔርወን','ኔርና',
'ኔሩኒ','ኔሩካ','ኔሩኪ','ኔሩኩም','ኔሩክን','ኔሩዎ','ኔሩዋ','ኔሩዎም','ኔሩወን','ኔሩና',
'ነሩኒ','ነሩካ','ነሩኪ','ነሩኩም','ነሩክን','ነሩዎ','ነሩዋ','ነሩዎም','ነሩወን','ነሩና',
'ነይሩኒ','ነይሩካ','ነይሩኪ','ነይሩኩም','ነይሩክን','ነይሩዎ','ነይሩዋ','ነይሩዎም','ነይሩወን','ነይሩና']

tigrinaModalPastVerbToBeNegative=[
'ኣይነበረንን','ኣይነበረካን','ኣይነበረክን','ኣይነበርኩምን','ኣይነበረክንን','ኣይነበሮን','ኣይነበራን','ኣይነበሮምን','ኣይነበረንን','ኣይነበረናን']

tigrina_modal_with_possiblity_negative=[
'ይኽእል','ትኽእል','ትኽእሉ','ትኽእላ','ትኽእል','ይኽእሉ','ይኽእላ','ንኽእል',
'ከምዝኽእል','ከምትኽእል','ከምትኽእሊ','ከምትኽእሉ','ከምትኽእላ','ከምዝኽእሉ','ከምዝኽእላ','ከምንኽእል',
'ከምዝክእል','ከምትክእል','ከምትክእሊ','ከምትክእሉ','ከምትክእላ','ከምዝክእሉ','ከምዝክእላ','ከምንክእል']

tigrinaModalWithPossiblityNegative=[
'ኣይክእልን','ኣይትኽእልን','ኣይትኽእሉን','ኣይትኽእላን','ኣይትኽእልን','ኣይክእሉን','ኣይክእላን','ኣይንኽእልን',
'ከምዘይኽእል','ከምዘይትኽእል','ከምዘይትኽእሊ','ከምዘይትኽእሉ','ከምዘይትኽእላ','ከምዘይኽእሉ','ከምዘይኽእላ','ከምዘይንኽእል',
'ከምዘይክእል','ከምዘይትክእል','ከምዘይትክእሊ','ከምዘይትክእሉ','ከምዘይትክእላ','ከምዘይክእሉ','ከምዘይክእላ','ከምዘይንክእል']

tigrina_modal_with_possiblity2=[
'ምኽኣልኩ','ምኽኣልካ','ምኽኣልኪ','ምኽኣለ','ምኽኣለት','ምኽኣልኩም','ምኽኣልክን','ምኽኣለ','ምኽኣሉ','ምኽኣላ','ምኽኣልና',
'ምኻኣልኩ','ምኻኣልካ','ምኻኣልኪ','ምኻኣለ','ምኻኣለት','ምኻኣልኩም','ምኻኣልክን','ምኻኣለ','ምኻኣሉ','ምኻኣላ','ምኻኣልና']

tigrina_modal_with_possiblity2_negative=[
'ኣይምኽኣልኩን','ኣይምኽኣልካን','ኣይምኽኣልክን','ኣይምኽኣለን','ኣይምኽኣለትን','ኣይምኽኣልኩምን','ኣይምኽኣልክንን','ኣይምኽኣለን','ኣይምኽኣሉን','ኣይምኽኣላን','ኣይምኽኣልናን']

tigrina_modal_with_possiblity_yikewin=[
'ድኾና','ድኾኑ','ድኸውን','ዝኸውን','ዝኾኑ','ዝኾና','ይኸውን','ትኸውን','ትኾኑ','ትኾና','ትኸውን','ይኾኑ','ይኾና','ንኸውን']

tigrina_modal_with_possiblity_yikewin_negative=[
'ኣይኸውንን','ኣይትኾኑን','ኣይትኾናን','ኣይትኸውንን','ኣይኾኑን','ኣይኾናን','ኣይንኸውንን']

tigrina_modal_with_possiblity_mikan=[
'ክኸውን','ክትከውን','ክትኮኒ','ክትኮና','ክትኮኑ','ክኾኑ','ክኾና','ክንከውን']


tigrina_modal_with_possiblity_mikan_negative=[
'ኣይክኸውንን','ኣይክትከውንን','ኣይክትኮንን','ኣይክኾናን','ኣይክትኮናን','ኣይከውንን','ኣይክትኮኑን','ኣይክትኮኑን','ኣይክንከውንን']

tigrina_modal_with_possiblity_mikone=[
'ምኾንካ','ምኾንኩ','ምኾነ','ምኾነት','ምኾንኪ','ምኾንክን','ምኾንኩም','ምኾኑ','ምኾና','ምኾንና']


tigrina_modal_with_possiblity_mikone_negative=[
'ኣይምኾንካን','ኣይምኾንኩን','ኣይምኾነን','ኣይምኾነትን','ኣይምኾንኪን','ኣይምኾንክንን','ኣይምኾንኩምን','ኣይምኾኑን','ኣይምኾናን','ኣይምኾንናን']
tigrina_modal_with_possiblity_kikiel=[
'ክኽእል','ክትክእል','ክትክእሊ','ክትክእሉ','ክትክእላ','ክትክእል','ክኽእሉ','ክኽእላ','ክንክእል']


zeykona= ['ዘይኮንኩ','ዘይኮንካ','ዘይኮንኪ','ዘይኮንኩም','ዘይኮንክን','ዘይኮነ','ዘይኮነት','ዘይኮኑ','ዘይኮና','ዘይኮንና']

entekoyne= ['እንተኾይነ','እንተኾይንካ','እንተኾይንኪ','እንተኾይንኩም','እንተኾይንክን','እንተኾይኑ','እንተኾይና','እንተኾኑ','እንተኾና','እንተኾይና','እንተኾነ',
'እንተኮይነ','እንተኮይንካ','እንተኮይንኪ','እንተኮይንኩም','እንተኮይንክን','እንተኮይኑ','እንተኮይና','እንተኮይኖም','እንተኮይነን','እንተኮይንና',
'እንተኾይነ','እንተኾይንካ','እንተኾይንኪ','እንተኾይንኩም','እንተኾይንክን','እንተኾይኑ','እንተኾይና','እንተኾይኖም','እንተኾይነን','እንተኾይንና']

ente_zeykoyna= ['ካብዘይኮንኩ','ካብዘይኮንካ','ካብዘይኮንኪ','ካብዘይኮንኩም','ካብዘይኮንክን','ካብዘይኮነ','ካብዘይኮነት','ካብዘይኮኑ','ካብዘይኮና','ካብዘይኮንና',
'እንተዘይኮይነ','እንተዘይኮይንካ','እንተዘይኮይንኪ','እንተዘይኮይንኩም','እንተዘይኮይንክን','እንተዘይኮይኑ','እንተዘይኮይና','እንተዘይኮይኖም','እንተዘይኮይነን','እንተዘይኮይንና',
'እንተዘይኮንኩ','እንተዘይኮንካ','እንተዘይኮንኪ','እንተዘይኮንኩም','እንተዘይኮንክን','እንተዘይኮነ','እንተዘይኮነት','እንተዘይኮኑ','እንተዘይኮና','እንተዘይኮንና']



kabkone= ['ካብኮንኩ','ካብኮንካ','ካብኮንኪ','ካብኮንኩም','ካብኮንክን','ካብኮነ','ካብኮነት','ካብኮኑ','ካብኮና','ካብኮንና']
zeymkona= ['ዘይምዃነይ','ዘይምዃንካ','ዘይምዃንኪ','ዘይምዃንኩም','ዘይምዃንክን','ዘይምዃኑ','ዘይምዃና','ዘይምዃኖም','ዘይምዃነን','ዘይምዃና']
koyne= ['ኮይነ','ኮይንካ','ኮይንኪ','ኮይንኩም','ኮይንክን','ኮይኑ','ኮይና','ኮይኖም','ኮይነን','ኮይንና']
kone= ['ኮንኩ','ኮንካ','ኮንኪ','ኮንኩም','ኮንክን','ኮነ','ኮነት','ኮኑ','ኮና','ኮንና']
keykone= ['ከይኮንኩ','ከይኮንካ','ከይኮንኪ','ከይኮንኩም','ከይኮንክን','ከይኮነ','ከይኮነት','ከይኮኑ','ከይኮና','ከይኮንና']
zeykealku= ['ዘይከኣልኩ','ዘይከኣልካ','ዘይከኣልኪ','ዘይከኣልኩም','ዘይከኣልክን','ዘይከኣለ','ዘይከኣለት','ዘይከኣሉ','ዘይከኣላ','ዘይከኣልና']
kealku= ['ከኣልኩ','ከኣልካ','ከኣልኪ','ከኣልኩም','ከኣልክን','ከኣለ','ከኣለት','ከኣሉ','ከኣላ','ከኣልና']
zeymkaaley= ['ዘይምኽኣለይ','ዘይምኽኣልካ','ዘይምኽኣልኪ','ዘይምኽኣልኩም','ዘይምኽኣልክን','ዘይምኽኣሉ','ዘይምኽኣላ','ዘይምኽኣሎም','ዘይምኽኣለን','ዘይምኽኣልና','ዘይምኽኣል']
zeykiel= ['ዘይክእል','ዘይትኽእል','ዘይትኽእሊ','ዘይትኽእሉ','ዘይትኽእላ','ዘይክእል','ዘይትኽእል','ዘይኽእሉ','ዘይክእላ','ዘይንኽእል']
keykaale=['ከይከኣልኩ','ከይክኣልካ','ከይክኣልኪ','ከይክኣልኩም','ከይክኣልክን','ከይክኣለ','ከይክኣለት','ከይክኣሉ','ከይክኣላ','ከይክኣልና']
keykaale_2=['ከይከኣልኩ ከለኹ','ከይክኣልካ ከለኻ','ከይክኣልኪ ከለኺ','ከይክኣልኩም ከለኹም','ከይክኣልክን ከለኽን','ከይክኣለ ከሎ','ከይክኣለት ከላ','ከይክኣሉ ከለዉ','ከይክኣላ ከለዋ','ከይክኣልና ከለና']


common_first_letters_on_modal=[
'ት','ክ','ይ','ከ','ክት','ኣይ','ዘይ','ከይ','ም','መ','የ']
negative_starts=['ኣይ','ዘይ','ከይ']
common_first_letters_on_modal_past=['ም','ምስ']
common_first_letters_on_while=['ይ','ት','ን']

tigrinaModalCommon=['ይግባእ','ግድን']

tigrina_verb_to_be_with_verb=[
'ኣለኹ','ኣለኻ','ኣለኺ','ኣለኹም','ኣለኽን','ኣሎ','ኣላ','ኣለዉ','ኣለዋ','ኣለና']
verb_to_bes_obj = [
    { "id": 0, "tigrina": "እቲ", "english": "that" },
    { "id": 1, "tigrina": "እዚ", "english": "this" },
    { "id": 2, "tigrina": "እቲኦም", "english": "they" },
    { "id": 3, "tigrina": "እቶም", "english": "they" },
    { "id": 4, "tigrina": "እዚኦም", "english": "these" },
    { "id": 5, "tigrina": "እቲኤን", "english": "they" },
    { "id": 6, "tigrina": "እተን", "english": "they" },
    { "id": 7, "tigrina": "እዚኤን", "english": "these" },
    { "id": 8, "tigrina": "እዘን", "english": "these" },
    { "id": 9, "tigrina": "እቲኣቶም", "english": "they" },
    { "id": 10, "tigrina": "እቶም", "english": "they" },
    { "id": 11, "tigrina": "እቲኣተን", "english": "they" },
    { "id": 12, "tigrina": "እተን", "english": "the" },
    { "id": 13, "tigrina": "እዚኣቶም", "english": "these" },
    { "id": 14, "tigrina": "እዚኦም", "english": "these" },
    { "id": 15, "tigrina": "እዞም", "english": "these" },
    { "id": 16, "tigrina": "ነቲ", "english": "the one" },
    { "id": 17, "tigrina": "ነቶም", "english": "them" },
    { "id": 18, "tigrina": "ነተን", "english": "them" },
    { "id": 19, "tigrina": "ነታ", "english": "for her" },
    { "id": 20, "tigrina": "ነቲኦም", "english": "to them" },
    { "id": 21, "tigrina": "ነቲአን", "english": "them" },
    { "id": 22, "tigrina": "ነቲኣ", "english": "Netia" },
    { "id": 23, "tigrina": "ነቲኣቶም", "english": "them" },
    { "id": 24, "tigrina": "ነቲኣተን", "english": "them" },
    { "id": 25, "tigrina": "ንስኻ", "english": "you" },
    { "id": 26, "tigrina": "ንስኺ", "english": "you" },
    { "id": 27, "tigrina": "ንሱ", "english": "he" },
    { "id": 28, "tigrina": "ንሳ", "english": "she" },
    { "id": 29, "tigrina": "ኣነ", "english": "I" },
    { "id": 30, "tigrina": "ንሶም", "english": "they" },
    { "id": 31, "tigrina": "ንሰን", "english": "they" },
    { "id": 32, "tigrina": "ንሳቶም", "english": "they" },
    { "id": 33, "tigrina": "ንሳተን", "english": "they" },
    { "id": 34, "tigrina": "ንስኹም", "english": "you" },
    { "id": 35, "tigrina": "ንስኽን", "english": "you" },
    { "id": 36, "tigrina": "ንስኻትኩም", "english": "you" },
    { "id": 37, "tigrina": "ንስኻትክን", "english": "you and" },
    { "id": 38, "tigrina": "ንሕና", "english": "we" },
    { "id": 39, "tigrina": "ኣለኹ", "english": "I am" },
    { "id": 40, "tigrina": "ኣለኻ", "english": "you are" },
    { "id": 41, "tigrina": "ኣለኺ", "english": "you are" },
    { "id": 42, "tigrina": "ኣለኹም", "english": "you are" },
    { "id": 43, "tigrina": "ኣለኽን", "english": "you are" },
    { "id": 44, "tigrina": "ኣሎ", "english": "there" },
    { "id": 45, "tigrina": "ኣላ", "english": "there" },
    { "id": 46, "tigrina": "ኣለዉ", "english": "there are" },
    { "id": 47, "tigrina": "ኣለዋ", "english": "there" },
    { "id": 48, "tigrina": "ኣለና", "english": "we have" },
    { "id": 49, "tigrina": "ይግባእ", "english": "should" },
    { "id": 50, "tigrina": "ግድን", "english": "must" },
    { "id": 51, "tigrina": "ክኽእል", "english": "can" },
    { "id": 52, "tigrina": "ክትክእል", "english": "to be able" },
    { "id": 53, "tigrina": "ክትክእሊ", "english": "to be able" },
    { "id": 54, "tigrina": "ክትክእሉ", "english": "to be able" },
    { "id": 55, "tigrina": "ክትክእላ", "english": "to be able" },
    { "id": 56, "tigrina": "ክትክእል", "english": "to be able" },
    { "id": 57, "tigrina": "ክኽእሉ", "english": "to be able" },
    { "id": 58, "tigrina": "ክኽእላ", "english": "to be able" },
    { "id": 59, "tigrina": "ክንክእል", "english": "we can" },
    { "id": 60, "tigrina": "ኣይምኾንካን", "english": "you wouldn't be" },
    { "id": 61, "tigrina": "ኣይምኾንኩን", "english": "I wouldn't be" },
    { "id": 62, "tigrina": "ኣይምኾነን", "english": "wouldn't be" },
    { "id": 63, "tigrina": "ኣይምኾነትን", "english": "wouldn't be" },
    { "id": 64, "tigrina": "ኣይምኾንኪን", "english": "you wouldn't be" },
    { "id": 65, "tigrina": "ኣይምኾንክንን", "english": "you wouldn't be" },
    { "id": 66, "tigrina": "ኣይምኾንኩምን", "english": "you wouldn't be" },
    { "id": 67, "tigrina": "ኣይምኾኑን", "english": "They wouldn't be" },
    { "id": 68, "tigrina": "ኣይምኾናን", "english": "we wouldn't be" },
    { "id": 69, "tigrina": "ኣይምኾንናን", "english": "we wouldn't be" },
    { "id": 70, "tigrina": "ምኾንካ", "english": "you would be" },
    { "id": 71, "tigrina": "ምኾንኩ", "english": "I would be" },
    { "id": 72, "tigrina": "ምኾነ", "english": "would be" },
    { "id": 73, "tigrina": "ምኾነት", "english": "would be" },
    { "id": 74, "tigrina": "ምኾንኪ", "english": "you would be" },
    { "id": 75, "tigrina": "ምኾንክን", "english": "you would be" },
    { "id": 76, "tigrina": "ምኾንኩም", "english": "you would be" },
    { "id": 77, "tigrina": "ምኾኑ", "english": "would be" },
    { "id": 78, "tigrina": "ምኾና", "english": "would be" },
    { "id": 79, "tigrina": "ምኾንና", "english": "we would be" },
    { "id": 80, "tigrina": "ኣይክኸውንን", "english": "will not happen" },
    { "id": 81, "tigrina": "ኣይክትከውንን", "english": "You shall not be" },
    { "id": 82, "tigrina": "ኣይክትኮንን", "english": "You shall not be" },
    { "id": 83, "tigrina": "ኣይክኾናን", "english": "they won't be" },
    { "id": 84, "tigrina": "ኣይክትኮናን", "english": "they shall not be" },
    { "id": 85, "tigrina": "ኣይከውንን", "english": "not likely" },
    { "id": 86, "tigrina": "ኣይክትኮኑን", "english": "You shall not be" },
    { "id": 87, "tigrina": "ኣይክትኮኑን", "english": "you shall not be" },
    { "id": 88, "tigrina": "ኣይክንከውንን", "english": "we won't be" },
    { "id": 89, "tigrina": "ክኸውን", "english": "to be" },
    { "id": 90, "tigrina": "ክትከውን", "english": "to be" },
    { "id": 91, "tigrina": "ክትኮኒ", "english": "to be" },
    { "id": 92, "tigrina": "ክትኮና", "english": "to be" },
    { "id": 93, "tigrina": "ክትኮኑ", "english": "to be" },
    { "id": 94, "tigrina": "ክኾኑ", "english": "to be" },
    { "id": 95, "tigrina": "ክኾና", "english": "to be" },
    { "id": 96, "tigrina": "ክንከውን", "english": "to be" },
    { "id": 97, "tigrina": "ኣይኸውንን", "english": "not likely" },
    { "id": 98, "tigrina": "ኣይትኾኑን", "english": "you shall not be" },
    { "id": 99, "tigrina": "ኣይትኾናን", "english": "You will not be" },
    { "id": 100, "tigrina": "ኣይትኸውንን", "english": "You shall not" },
    { "id": 101, "tigrina": "ኣይኾኑን", "english": "They are not" },
    { "id": 102, "tigrina": "ኣይኾናን", "english": "we are not" },
    { "id": 103, "tigrina": "ኣይንኸውንን", "english": "We will not be" },
    { "id": 104, "tigrina": "ድኾና", "english": "we'll be" },
    { "id": 105, "tigrina": "ድኾኑ", "english": "be" },
    { "id": 106, "tigrina": "ድኸውን", "english": "will" },
    { "id": 107, "tigrina": "ዝኸውን", "english": "to be" },
    { "id": 108, "tigrina": "ዝኾኑ", "english": "who are" },
    { "id": 109, "tigrina": "ዝኾና", "english": "which" },
    { "id": 110, "tigrina": "ይኸውን", "english": "becomes" },
    { "id": 111, "tigrina": "ትኸውን", "english": "you become" },
    { "id": 112, "tigrina": "ትኾኑ", "english": "you'll be" },
    { "id": 113, "tigrina": "ትኾና", "english": "become" },
    { "id": 114, "tigrina": "ትኸውን", "english": "you become" },
    { "id": 115, "tigrina": "ይኾኑ", "english": "become" },
    { "id": 116, "tigrina": "ይኾና", "english": "become" },
    { "id": 117, "tigrina": "ንኸውን", "english": "we become" },
    { "id": 118, "tigrina": "ኣይምኽኣልኩን", "english": "I couldn't" },
    { "id": 119, "tigrina": "ኣይምኽኣልካን", "english": "you couldn't" },
    { "id": 120, "tigrina": "ኣይምኽኣልክን", "english": "you couldn't" },
    { "id": 121, "tigrina": "ኣይምኽኣለን", "english": "couldn't" },
    { "id": 122, "tigrina": "ኣይምኽኣለትን", "english": "couldn't" },
    { "id": 123, "tigrina": "ኣይምኽኣልኩምን", "english": "you couldn't" },
    { "id": 124, "tigrina": "ኣይምኽኣልክንን", "english": "you couldn't" },
    { "id": 125, "tigrina": "ኣይምኽኣለን", "english": "couldn't" },
    { "id": 126, "tigrina": "ኣይምኽኣሉን", "english": "they couldn't" },
    { "id": 127, "tigrina": "ኣይምኽኣላን", "english": "couldn't" },
    { "id": 128, "tigrina": "ኣይምኽኣልናን", "english": "we couldn't" },
    { "id": 129, "tigrina": "ምኽኣልኩ", "english": "I could" },
    { "id": 130, "tigrina": "ምኽኣልካ", "english": "your ability" },
    { "id": 131, "tigrina": "ምኽኣልኪ", "english": "your ability" },
    { "id": 132, "tigrina": "ምኽኣለ", "english": "enabling" },
    { "id": 133, "tigrina": "ምኽኣለት", "english": "enabling" },
    { "id": 134, "tigrina": "ምኽኣልኩም", "english": "your ability" },
    { "id": 135, "tigrina": "ምኽኣልክን", "english": "your ability" },
    { "id": 136, "tigrina": "ምኽኣለ", "english": "enabling" },
    { "id": 137, "tigrina": "ምኽኣሉ", "english": "being able" },
    { "id": 138, "tigrina": "ምኽኣላ", "english": "being able" },
    { "id": 139, "tigrina": "ምኽኣልና", "english": "we can" },
    { "id": 140, "tigrina": "ምኻኣልኩ", "english": "I could" },
    { "id": 141, "tigrina": "ምኻኣልካ", "english": "you could" },
    { "id": 142, "tigrina": "ምኻኣልኪ", "english": "you could" },
    { "id": 143, "tigrina": "ምኻኣለ", "english": "could" },
    { "id": 144, "tigrina": "ምኻኣለት", "english": "could" },
    { "id": 145, "tigrina": "ምኻኣልኩም", "english": "you could" },
    { "id": 146, "tigrina": "ምኻኣልክን", "english": "you could" },
    { "id": 147, "tigrina": "ምኻኣለ", "english": "could" },
    { "id": 148, "tigrina": "ምኻኣሉ", "english": "being able" },
    { "id": 149, "tigrina": "ምኻኣላ", "english": "being able" },
    { "id": 150, "tigrina": "ምኻኣልና", "english": "we could" },
    { "id": 151, "tigrina": "ኣይክእልን", "english": "I can't" },
    { "id": 152, "tigrina": "ኣይትኽእልን", "english": "you can't" },
    { "id": 153, "tigrina": "ኣይትኽእሉን", "english": "you can't" },
    { "id": 154, "tigrina": "ኣይትኽእላን", "english": "you can't" },
    { "id": 155, "tigrina": "ኣይትኽእልን", "english": "you can't" },
    { "id": 156, "tigrina": "ኣይክእሉን", "english": "they can't" },
    { "id": 157, "tigrina": "ኣይክእላን", "english": "can't" },
    { "id": 158, "tigrina": "ኣይንኽእልን", "english": "we can't" },
    { "id": 159, "tigrina": "ከምዘይኽእል", "english": "that it cannot" },
    { "id": 160, "tigrina": "ከምዘይትኽእል", "english": "that you can't" },
    { "id": 161, "tigrina": "ከምዘይትኽእሊ", "english": "that you can't" },
    { "id": 162, "tigrina": "ከምዘይትኽእሉ", "english": "that you cannot" },
    { "id": 163, "tigrina": "ከምዘይትኽእላ", "english": "as if she couldn't" },
    { "id": 164, "tigrina": "ከምዘይኽእሉ", "english": "that they cannot" },
    { "id": 165, "tigrina": "ከምዘይኽእላ", "english": "that they cannot" },
    { "id": 166, "tigrina": "ከምዘይንኽእል", "english": "that we cannot" },
    { "id": 167, "tigrina": "ከምዘይክእል", "english": "that I cannot" },
    { "id": 168, "tigrina": "ከምዘይትክእል", "english": "that you can't" },
    { "id": 169, "tigrina": "ከምዘይትክእሊ", "english": "that you can't" },
    { "id": 170, "tigrina": "ከምዘይትክእሉ", "english": "that you cannot" },
    { "id": 171, "tigrina": "ከምዘይትክእላ", "english": "that she cannot" },
    { "id": 172, "tigrina": "ከምዘይክእሉ", "english": "that they cannot" },
    { "id": 173, "tigrina": "ከምዘይክእላ", "english": "that they cannot" },
    { "id": 174, "tigrina": "ከምዘይንክእል", "english": "that we cannot" },
    { "id": 175, "tigrina": "ይኽእል", "english": "can" },
    { "id": 176, "tigrina": "ትኽእል", "english": "you can" },
    { "id": 177, "tigrina": "ትኽእሉ", "english": "you can" },
    { "id": 178, "tigrina": "ትኽእላ", "english": "you can" },
    { "id": 179, "tigrina": "ትኽእል", "english": "you can" },
    { "id": 180, "tigrina": "ይኽእሉ", "english": "can" },
    { "id": 181, "tigrina": "ይኽእላ", "english": "can" },
    { "id": 182, "tigrina": "ንኽእል", "english": "we can" },
    { "id": 183, "tigrina": "ከምዝኽእል", "english": "as can" },
    { "id": 184, "tigrina": "ከምትኽእል", "english": "as you can" },
    { "id": 185, "tigrina": "ከምትኽእሊ", "english": "as you can" },
    { "id": 186, "tigrina": "ከምትኽእሉ", "english": "as you can" },
    { "id": 187, "tigrina": "ከምትኽእላ", "english": "as you can" },
    { "id": 188, "tigrina": "ከምዝኽእሉ", "english": "as they can" },
    { "id": 189, "tigrina": "ከምዝኽእላ", "english": "as they can" },
    { "id": 190, "tigrina": "ከምንኽእል", "english": "as we can" },
    { "id": 191, "tigrina": "ከምዝክእል", "english": "as I can" },
    { "id": 192, "tigrina": "ከምትክእል", "english": "as you can" },
    { "id": 193, "tigrina": "ከምትክእሊ", "english": "as you can" },
    { "id": 194, "tigrina": "ከምትክእሉ", "english": "as you can" },
    { "id": 195, "tigrina": "ከምትክእላ", "english": "as you can" },
    { "id": 196, "tigrina": "ከምዝክእሉ", "english": "as they can" },
    { "id": 197, "tigrina": "ከምዝክእላ", "english": "as they can" },
    { "id": 198, "tigrina": "ከምንክእል", "english": "as we can" },
    { "id": 199, "tigrina": "ኣይነበረንን", "english": "I did'n't have it" },
    { "id": 200, "tigrina": "ኣይነበረካን", "english": "you did'n't have it" },
    { "id": 201, "tigrina": "ኣይነበረክን", "english": "you weren't" },
    { "id": 202, "tigrina": "ኣይነበርኩምን", "english": "you were not" },
    { "id": 203, "tigrina": "ኣይነበረክንን", "english": "I didn't have it" },
    { "id": 204, "tigrina": "ኣይነበሮን", "english": "didn't have it" },
    { "id": 205, "tigrina": "ኣይነበራን", "english": "she didn't have" },
    { "id": 206, "tigrina": "ኣይነበሮምን", "english": "They did'n't have it" },
    { "id": 207, "tigrina": "ኣይነበረንን", "english": "I didn't have it" },
    { "id": 208, "tigrina": "ኣይነበረናን", "english": "we didn't have" },
    { "id": 209, "tigrina": "ኔርኒ", "english": "I had" },
    { "id": 210, "tigrina": "ኔርካ", "english": "were" },
    { "id": 211, "tigrina": "ኔርኪ", "english": "were" },
    { "id": 212, "tigrina": "ኔርኩም", "english": "were" },
    { "id": 213, "tigrina": "ኔርክን", "english": "Nerkn" },
    { "id": 214, "tigrina": "ኔርዎ", "english": "had" },
    { "id": 215, "tigrina": "ኔርዋ", "english": "had" },
    { "id": 216, "tigrina": "ኔርዎም", "english": "had" },
    { "id": 217, "tigrina": "ኔርወን", "english": "they had" },
    { "id": 218, "tigrina": "ኔርና", "english": "we were" },
    { "id": 219, "tigrina": "ኔሩኒ", "english": "I had" },
    { "id": 220, "tigrina": "ኔሩካ", "english": "Neruka" },
    { "id": 221, "tigrina": "ኔሩኪ", "english": "Neruki" },
    { "id": 222, "tigrina": "ኔሩኩም", "english": "you had" },
    { "id": 223, "tigrina": "ኔሩክን", "english": "Nerukn" },
    { "id": 224, "tigrina": "ኔሩዎ", "english": "had" },
    { "id": 225, "tigrina": "ኔሩዋ", "english": "had" },
    { "id": 226, "tigrina": "ኔሩዎም", "english": "had" },
    { "id": 227, "tigrina": "ኔሩወን", "english": "had" },
    { "id": 228, "tigrina": "ኔሩና", "english": "we had" },
    { "id": 229, "tigrina": "ነሩኒ", "english": "I had" },
    { "id": 230, "tigrina": "ነሩካ", "english": "Neruka" },
    { "id": 231, "tigrina": "ነሩኪ", "english": "Neruki" },
    { "id": 232, "tigrina": "ነሩኩም", "english": "you had" },
    { "id": 233, "tigrina": "ነሩክን", "english": "Nerukn" },
    { "id": 234, "tigrina": "ነሩዎ", "english": "had" },
    { "id": 235, "tigrina": "ነሩዋ", "english": "Neruwa" },
    { "id": 236, "tigrina": "ነሩዎም", "english": "had" },
    { "id": 237, "tigrina": "ነሩወን", "english": "they had" },
    { "id": 238, "tigrina": "ነሩና", "english": "we had" },
    { "id": 239, "tigrina": "ነይሩኒ", "english": "I had" },
    { "id": 240, "tigrina": "ነይሩካ", "english": "you had" },
    { "id": 241, "tigrina": "ነይሩኪ", "english": "neiruki" },
    { "id": 242, "tigrina": "ነይሩኩም", "english": "you had" },
    { "id": 243, "tigrina": "ነይሩክን", "english": "Neirukn" },
    { "id": 244, "tigrina": "ነይሩዎ", "english": "had" },
    { "id": 245, "tigrina": "ነይሩዋ", "english": "had" },
    { "id": 246, "tigrina": "ነይሩዎም", "english": "had" },
    { "id": 247, "tigrina": "ነይሩወን", "english": "had" },
    { "id": 248, "tigrina": "ነይሩና", "english": "we had" },
    { "id": 249, "tigrina": "የብለይን", "english": "I don't have" },
    { "id": 250, "tigrina": "የብልካን", "english": "you don't have" },
    { "id": 251, "tigrina": "የብልክን", "english": "you don't have" },
    { "id": 252, "tigrina": "የብልኩምን", "english": "you don't have" },
    { "id": 253, "tigrina": "የብልክንን", "english": "you don't have" },
    { "id": 254, "tigrina": "የብሉን", "english": "none" },
    { "id": 255, "tigrina": "የብላን", "english": "doesn't have" },
    { "id": 256, "tigrina": "የብሎምን", "english": "They don't have" },
    { "id": 257, "tigrina": "የብለንን", "english": "They don't have" },
    { "id": 258, "tigrina": "የብልናን", "english": "we don't have" },
    { "id": 259, "tigrina": "ኣለኒ", "english": "I have" },
    { "id": 260, "tigrina": "ኣለካ", "english": "you have" },
    { "id": 261, "tigrina": "ኣለኪ", "english": "you have" },
    { "id": 262, "tigrina": "ኣለኩም", "english": "you have" },
    { "id": 263, "tigrina": "ኣለክን", "english": "you have" },
    { "id": 264, "tigrina": "ኣለዎ", "english": "has" },
    { "id": 265, "tigrina": "ኣለዋ", "english": "there" },
    { "id": 266, "tigrina": "ኣለዎም", "english": "have" },
    { "id": 267, "tigrina": "ኣለወን", "english": "They have" },
    { "id": 268, "tigrina": "ኣለና", "english": "we have" },
    { "id": 269, "tigrina": "ኣይክህልወካን", "english": "you shall not have" },
    { "id": 270, "tigrina": "ኣይክህልወኒን", "english": "I won't have it" },
    { "id": 271, "tigrina": "ኣይክህልዎን", "english": "will not have" },
    { "id": 272, "tigrina": "ኣይክህልዋን", "english": "will not have" },
    { "id": 273, "tigrina": "ኣይክህልወኪን", "english": "you shall not have" },
    { "id": 274, "tigrina": "ኣይክህልወኩምን", "english": "you shall not have" },
    { "id": 275, "tigrina": "ኣይክህልወክንን", "english": "I shall not have you" },
    { "id": 276, "tigrina": "ኣይክህልዎምን", "english": "They shall not have" },
    { "id": 277, "tigrina": "ኣይክህልወንን", "english": "I won't have it" },
    { "id": 278, "tigrina": "ኣይክህልወናን", "english": "we won't have it" },
    { "id": 279, "tigrina": "ክህልወካ", "english": "to have" },
    { "id": 280, "tigrina": "ክህልወኒ", "english": "to have" },
    { "id": 281, "tigrina": "ክህልዎ", "english": "to have" },
    { "id": 282, "tigrina": "ክህልዋ", "english": "to have" },
    { "id": 283, "tigrina": "ክህልወኪ", "english": "to have" },
    { "id": 284, "tigrina": "ክህልወኩም", "english": "to have" },
    { "id": 285, "tigrina": "ክህልወክን", "english": "to have" },
    { "id": 286, "tigrina": "ክህልዎም", "english": "to have" },
    { "id": 287, "tigrina": "ክህልወን", "english": "to have" },
    { "id": 288, "tigrina": "ክህልወና", "english": "to have" },
    { "id": 289, "tigrina": "ኣይነበርኩን", "english": "I wasn't" },
    { "id": 290, "tigrina": "ኣይነበርካን", "english": "you weren't" },
    { "id": 291, "tigrina": "ኣይነበርክን", "english": "you weren't" },
    { "id": 292, "tigrina": "ኣይነበርኩምን", "english": "you were not" },
    { "id": 293, "tigrina": "ኣይነበርክን", "english": "you weren't" },
    { "id": 294, "tigrina": "ኣይነበረን", "english": "wasn't there" },
    { "id": 295, "tigrina": "ኣይነበረትን", "english": "wasn't there" },
    { "id": 296, "tigrina": "ኣይነበሩን", "english": "were not" },
    { "id": 297, "tigrina": "ኣይነበራን", "english": "she didn't have" },
    { "id": 298, "tigrina": "ኣይነበርናን", "english": "we weren't" },
    { "id": 299, "tigrina": "ኔረ", "english": "I was" },
    { "id": 300, "tigrina": "ኔርካ", "english": "were" },
    { "id": 301, "tigrina": "ኔርኪ", "english": "were" },
    { "id": 302, "tigrina": "ኔርኩም", "english": "were" },
    { "id": 303, "tigrina": "ኔርክን", "english": "Nerkn" },
    { "id": 304, "tigrina": "ኔሩ", "english": "was" },
    { "id": 305, "tigrina": "ኔራ", "english": "was" },
    { "id": 306, "tigrina": "ኔሮም", "english": "were" },
    { "id": 307, "tigrina": "ኔረን", "english": "were" },
    { "id": 308, "tigrina": "ኔርና", "english": "we were" },
    { "id": 309, "tigrina": "ነረ", "english": "was" },
    { "id": 310, "tigrina": "ነርካ", "english": "were" },
    { "id": 311, "tigrina": "ነርኪ", "english": "were" },
    { "id": 312, "tigrina": "ነርኩም", "english": "were" },
    { "id": 313, "tigrina": "ነርክን", "english": "Nerk" },
    { "id": 314, "tigrina": "ነሩ", "english": "there were" },
    { "id": 315, "tigrina": "ነራ", "english": "was" },
    { "id": 316, "tigrina": "ነሮም", "english": "were" },
    { "id": 317, "tigrina": "ነረን", "english": "were" },
    { "id": 318, "tigrina": "ነርና", "english": "we were" },
    { "id": 319, "tigrina": "ነይረ", "english": "I was" },
    { "id": 320, "tigrina": "ነይርካ", "english": "were" },
    { "id": 321, "tigrina": "ነይርኪ", "english": "you were" },
    { "id": 322, "tigrina": "ነይርኩም", "english": "were" },
    { "id": 323, "tigrina": "ነይርክን", "english": "you were" },
    { "id": 324, "tigrina": "ነይሩ", "english": "was" },
    { "id": 325, "tigrina": "ነይራ", "english": "was" },
    { "id": 326, "tigrina": "ነይሮም", "english": "were" },
    { "id": 327, "tigrina": "ነይረን", "english": "were" },
    { "id": 328, "tigrina": "ነይርና", "english": "we were" },
    { "id": 329, "tigrina": "ኣይኮንኩን", "english": "I'm not" },
    { "id": 330, "tigrina": "ኣይኮንካን", "english": "You're not" },
    { "id": 331, "tigrina": "ኣይኮንክን", "english": "You're not" },
    { "id": 332, "tigrina": "ኣይኮንኩምን", "english": "You are not" },
    { "id": 333, "tigrina": "ኣይኮንክንን", "english": "I'm not" },
    { "id": 334, "tigrina": "ኣይኮነን", "english": "not" },
    { "id": 335, "tigrina": "ኣይኮንክን", "english": "You're not" },
    { "id": 336, "tigrina": "ኣይኮኑን", "english": "They are not" },
    { "id": 337, "tigrina": "ኣይኮናን", "english": "We are not" },
    { "id": 338, "tigrina": "ኣይኮንናን", "english": "We are not" },
    { "id": 339, "tigrina": "ት", "english": "t" },
    { "id": 340, "tigrina": "ክ", "english": "k" },
    { "id": 341, "tigrina": "ይ", "english": "y" },
    { "id": 342, "tigrina": "ዝ", "english": "z" },
    { "id": 343, "tigrina": "ኢየ", "english": "I" },
    { "id": 344, "tigrina": "ኢኻ", "english": "you" },
    { "id": 345, "tigrina": "ኢኺ", "english": "you" },
    { "id": 346, "tigrina": "ኢኹም", "english": "you" },
    { "id": 347, "tigrina": "ኢኽን", "english": "you" },
    { "id": 348, "tigrina": "ኢዩ", "english": "EU" },
    { "id": 349, "tigrina": "ኢያ", "english": "Iya" },
    { "id": 350, "tigrina": "ኢዮም", "english": "they" },
    { "id": 351, "tigrina": "ኢየን", "english": "they" },
    { "id": 352, "tigrina": "ኢና", "english": "we" },
    { "id": 353, "tigrina": "ዝነበርካ", "english": "you were" },
    { "id": 354, "tigrina": "ዝነበርኪ", "english": "you were" },
    { "id": 355, "tigrina": "ዝነበርኩም", "english": "you were" },
    { "id": 356, "tigrina": "ዝነበርክን", "english": "you were" },
    { "id": 357, "tigrina": "ዝነበረ", "english": "was" },
    { "id": 358, "tigrina": "ዝነበረት", "english": "was" },
    { "id": 359, "tigrina": "ዝነበርኩ", "english": "I lived" },
    { "id": 360, "tigrina": "ዝነበሩ", "english": "who were" },
    { "id": 361, "tigrina": "ዝነበራ", "english": "had" },
    { "id": 362, "tigrina": "ዝነበርና", "english": "we lived" },
    { "id": 363, "tigrina": "ዘለኻ", "english": "you are" },
    { "id": 364, "tigrina": "ዘለኺ", "english": "you are" },
    { "id": 365, "tigrina": "ዘለኹም", "english": "you are" },
    { "id": 366, "tigrina": "ዘለኽን", "english": "you have" },
    { "id": 367, "tigrina": "ዘሎ", "english": "existing" },
    { "id": 369, "tigrina": "ዘለኹ", "english": "I am" },
    { "id": 370, "tigrina": "ዘለዉ", "english": "existing" },
    { "id": 371, "tigrina": "ዘለዋ", "english": "having" },
    { "id": 372, "tigrina": "ዘለና", "english": "we have" },
    { "id": 373, "tigrina": "ከለኻ", "english": "while" },
    { "id": 374, "tigrina": "ከለኺ", "english": "when you" },
    { "id": 375, "tigrina": "ከለኹም", "english": "while" },
    { "id": 376, "tigrina": "ከለኽን", "english": "when" },
    { "id": 377, "tigrina": "ከሎ", "english": "while" },
    { "id": 378, "tigrina": "ከላ", "english": "while" },
    { "id": 379, "tigrina": "ከለኹ", "english": "while" },
    { "id": 380, "tigrina": "ከለዉ", "english": "while" },
    { "id": 381, "tigrina": "ከለዋ", "english": "while1" },
    { "id": 383, "tigrina": "ዶ", "english": "do" },
    { "id": 384, "tigrina": "ድየ", "english": "Die" },
    { "id": 385, "tigrina": "ዲኻ", "english": "are you" },
    { "id": 386, "tigrina": "ዲኺ", "english": "Are you" },
    { "id": 387, "tigrina": "ዲኹም", "english": "are you" },
    { "id": 388, "tigrina": "ዲኽን", "english": "are you" },
    { "id": 389, "tigrina": "ድዩ", "english": "do" },
    { "id": 390, "tigrina": "ድያ", "english": "dia" },
    { "id": 391, "tigrina": "ድዮም", "english": "are they" },
    { "id": 392, "tigrina": "ድየን", "english": "Dien" },
    { "id": 393, "tigrina": "ዲና", "english": "Dinah" },
    { "id": 394, "tigrina": "ዲየ", "english": "Die" },
    { "id": 395, "tigrina": "ድኻ", "english": "poor" },
    { "id": 396, "tigrina": "ድኺ", "english": "poor" },
    { "id": 397, "tigrina": "ድኹም", "english": "weak" },
    { "id": 398, "tigrina": "ድኽን", "english": "poor" },
    { "id": 399, "tigrina": "ዲዩ", "english": "DU" },
    { "id": 400, "tigrina": "ዲያ", "english": "dia" },
    { "id": 401, "tigrina": "ዲዮም", "english": "Diom" },
    { "id": 402, "tigrina": "ዲየን", "english": "Dien" },
    { "id": 403, "tigrina": "ድና", "english": "Dna" },
    { "id": 404, "tigrina": "ዝኸውን", "english": "to be" },
    { "id": 405, "tigrina": "ርሕቐት", "english": "distance" },
    { "id": 406, "tigrina": "ምስ", "english": "with" },
    { "id": 407, "tigrina": "ንመን", "english": "to whom" },
    { "id": 408, "tigrina": "እንታይ", "english": "what" },
    { "id": 409, "tigrina": "ኣበይ", "english": "where" },
    { "id": 410, "tigrina": "በየን", "english": "where" },
    { "id": 411, "tigrina": "በየናይ", "english": "by which" },
    { "id": 412, "tigrina": "በበይ", "english": "where" },
    { "id": 413, "tigrina": "ናበይ", "english": "where" },
    { "id": 414, "tigrina": "ካበይ", "english": "from" },
    { "id": 415, "tigrina": "nabeyenay", "english": "nabeyenay" },
    { "id": 416, "tigrina": "ናበየናይ", "english": "to which" },
    { "id": 417, "tigrina": "ከመይ", "english": "how" },
    { "id": 418, "tigrina": "ብኸመይ", "english": "How" },
    { "id": 419, "tigrina": "ብከመይ", "english": "how" },
    { "id": 420, "tigrina": "መዓስ", "english": "when" },
    { "id": 421, "tigrina": "መን", "english": "who" },
    { "id": 422, "tigrina": "ክንደይ", "english": "how much" },
    { "id": 423, "tigrina": "ኣየናይ", "english": "which" },
    { "id": 424, "tigrina": "ስለምንታይ", "english": "why" },
    { "id": 425, "tigrina": "ክንደይ ዝኸውን", "english": "how much" },
    { "id": 426, "tigrina": "መበል ክንደይ", "english": "how many" },
    { "id": 427, "tigrina": "ምስ መን", "english": "with whom" },
    { "id": 428, "tigrina": "ዘይኮንኩ", "english": "not" },
    { "id": 429, "tigrina": "ዘይኮንካ", "english": "you are not" },
    { "id": 430, "tigrina": "ዘይኮንኪ", "english": "you're not" },
    { "id": 431, "tigrina": "ዘይኮንኩም", "english": "you are not" },
    { "id": 432, "tigrina": "ዘይኮንክን", "english": "You are not" },
    { "id": 433, "tigrina": "ዘይኮነ", "english": "not" },
    { "id": 434, "tigrina": "ዘይኮነት", "english": "not" },
    { "id": 435, "tigrina": "ዘይኮኑ", "english": "not" },
    { "id": 436, "tigrina": "ዘይኮና", "english": "not" },
    { "id": 437, "tigrina": "ዘይኮንና", "english": "we are not" },
    { "id": 439, "tigrina": "እንተኾይንካ", "english": "if you" },
    { "id": 440, "tigrina": "እንተኾይንኪ", "english": "if you" },
    { "id": 441, "tigrina": "እንተኾይንኩም", "english": "if you" },
    { "id": 442, "tigrina": "እንተኾይንክን", "english": "if you" },
    { "id": 443, "tigrina": "እንተኾይኑ", "english": "if" },
    { "id": 444, "tigrina": "እንተኾይና", "english": "if" },
    { "id": 368, "tigrina": "ዘላ", "english": "existing" },
    { "id": 369, "tigrina": "ዘለኹ", "english": "I am" },
    { "id": 370, "tigrina": "ዘለዉ", "english": "existing" },
    { "id": 371, "tigrina": "ዘለዋ", "english": "having" },
    { "id": 372, "tigrina": "ዘለና", "english": "we have" },
    { "id": 373, "tigrina": "ከለኻ", "english": "while" },
    { "id": 374, "tigrina": "ከለኺ", "english": "when you" },
    { "id": 375, "tigrina": "ከለኹም", "english": "while" },
    { "id": 376, "tigrina": "ከለኽን", "english": "when" },
    { "id": 377, "tigrina": "ከሎ", "english": "while" },
    { "id": 378, "tigrina": "ከላ", "english": "while" },
    { "id": 379, "tigrina": "ከለኹ", "english": "while" },
    { "id": 380, "tigrina": "ከለዉ", "english": "while" },
    { "id": 381, "tigrina": "ከለዋ", "english": "while1" },
    { "id": 383, "tigrina": "ዶ", "english": "do" },
    { "id": 384, "tigrina": "ድየ", "english": "Die" },
    { "id": 385, "tigrina": "ዲኻ", "english": "are you" },
    { "id": 386, "tigrina": "ዲኺ", "english": "Are you" },
    { "id": 387, "tigrina": "ዲኹም", "english": "are you" },
    { "id": 388, "tigrina": "ዲኽን", "english": "are you" },
    { "id": 389, "tigrina": "ድዩ", "english": "do" },
    { "id": 390, "tigrina": "ድያ", "english": "dia" },
    { "id": 391, "tigrina": "ድዮም", "english": "are they" },
    { "id": 392, "tigrina": "ድየን", "english": "Dien" },
    { "id": 393, "tigrina": "ዲና", "english": "Dinah" },
    { "id": 394, "tigrina": "ዲየ", "english": "Die" },
    { "id": 395, "tigrina": "ድኻ", "english": "poor" },
    { "id": 396, "tigrina": "ድኺ", "english": "poor" },
    { "id": 397, "tigrina": "ድኹም", "english": "weak" },
    { "id": 398, "tigrina": "ድኽን", "english": "poor" },
    { "id": 399, "tigrina": "ዲዩ", "english": "DU" },
    { "id": 400, "tigrina": "ዲያ", "english": "dia" },
    { "id": 401, "tigrina": "ዲዮም", "english": "Diom" },
    { "id": 402, "tigrina": "ዲየን", "english": "Dien" },
    { "id": 403, "tigrina": "ድና", "english": "Dna" },
    { "id": 404, "tigrina": "ዝኸውን", "english": "to be" },
    { "id": 405, "tigrina": "ርሕቐት", "english": "distance" },
    { "id": 406, "tigrina": "ምስ", "english": "with" },
    { "id": 407, "tigrina": "ንመን", "english": "to whom" },
    { "id": 408, "tigrina": "እንታይ", "english": "what" },
    { "id": 409, "tigrina": "ኣበይ", "english": "where" },
    { "id": 410, "tigrina": "በየን", "english": "where" },
    { "id": 411, "tigrina": "በየናይ", "english": "by which" },
    { "id": 412, "tigrina": "በበይ", "english": "where" },
    { "id": 413, "tigrina": "ናበይ", "english": "where" },
    { "id": 414, "tigrina": "ካበይ", "english": "from" },
    { "id": 415, "tigrina": "nabeyenay", "english": "nabeyenay" },
    { "id": 416, "tigrina": "ናበየናይ", "english": "to which" },
    { "id": 417, "tigrina": "ከመይ", "english": "how" },
    { "id": 418, "tigrina": "ብኸመይ", "english": "How" },
    { "id": 419, "tigrina": "ብከመይ", "english": "how" },
    { "id": 420, "tigrina": "መዓስ", "english": "when" },
    { "id": 421, "tigrina": "መን", "english": "who" },
    { "id": 422, "tigrina": "ክንደይ", "english": "how much" },
    { "id": 423, "tigrina": "ኣየናይ", "english": "which" },
    { "id": 424, "tigrina": "ስለምንታይ", "english": "why" },
    { "id": 425, "tigrina": "ክንደይ ዝኸውን", "english": "how much" },
    { "id": 426, "tigrina": "መበል ክንደይ", "english": "how many" },
    { "id": 427, "tigrina": "ምስ መን", "english": "with whom" },
    { "id": 428, "tigrina": "ዘይኮንኩ", "english": "not" },
    { "id": 429, "tigrina": "ዘይኮንካ", "english": "you are not" },
    { "id": 430, "tigrina": "ዘይኮንኪ", "english": "you're not" },
    { "id": 431, "tigrina": "ዘይኮንኩም", "english": "you are not" },
    { "id": 432, "tigrina": "ዘይኮንክን", "english": "You are not" },
    { "id": 433, "tigrina": "ዘይኮነ", "english": "not" },
    { "id": 434, "tigrina": "ዘይኮነት", "english": "not" },
    { "id": 435, "tigrina": "ዘይኮኑ", "english": "not" },
    { "id": 436, "tigrina": "ዘይኮና", "english": "not" },
    { "id": 437, "tigrina": "ዘይኮንና", "english": "we are not" },
    { "id": 438, "tigrina": "እንተኾይነ", "english": "If I" },
    { "id": 439, "tigrina": "እንተኾይንካ", "english": "if you" },
    { "id": 440, "tigrina": "እንተኾይንኪ", "english": "if you" },
    { "id": 441, "tigrina": "እንተኾይንኩም", "english": "if you" },
    { "id": 442, "tigrina": "እንተኾይንክን", "english": "if you" },
    { "id": 443, "tigrina": "እንተኾይኑ", "english": "if" },
    { "id": 444, "tigrina": "እንተኾይና", "english": "if" },
    { "id": 445, "tigrina": "እንተኾኑ", "english": "if" },
    { "id": 446, "tigrina": "እንተኾና", "english": "if" },
    { "id": 447, "tigrina": "እንተኾይና", "english": "if" },
    { "id": 448, "tigrina": "እንተኾነ", "english": "however" },
    { "id": 449, "tigrina": "እንተኮይነ", "english": "If I" },
    { "id": 450, "tigrina": "እንተኮይንካ", "english": "if you" },
    { "id": 451, "tigrina": "እንተኮይንኪ", "english": "if you" },
    { "id": 452, "tigrina": "እንተኮይንኩም", "english": "if you" },
    { "id": 453, "tigrina": "እንተኮይንክን", "english": "if you" },
    { "id": 454, "tigrina": "እንተኮይኑ", "english": "if" },
    { "id": 455, "tigrina": "እንተኮይና", "english": "if" },
    { "id": 456, "tigrina": "እንተኮይኖም", "english": "if they" },
    { "id": 457, "tigrina": "እንተኮይነን", "english": "if they are" },
    { "id": 458, "tigrina": "እንተኮይንና", "english": "if we" },
    { "id": 459, "tigrina": "እንተኾይነ", "english": "If I" },
    { "id": 460, "tigrina": "እንተኾይንካ", "english": "if you" },
    { "id": 461, "tigrina": "እንተኾይንኪ", "english": "if you" },
    { "id": 462, "tigrina": "እንተኾይንኩም", "english": "if you" },
    { "id": 463, "tigrina": "እንተኾይንክን", "english": "if you" },
    { "id": 464, "tigrina": "እንተኾይኑ", "english": "if" },
    { "id": 465, "tigrina": "እንተኾይና", "english": "if" },
    { "id": 466, "tigrina": "እንተኾይኖም", "english": "if they" },
    { "id": 467, "tigrina": "እንተኾይነን", "english": "if they are" },
    { "id": 468, "tigrina": "እንተኾይንና", "english": "if we" },
    { "id": 445, "tigrina": "እንተኾኑ", "english": "if" },
    { "id": 446, "tigrina": "እንተኾና", "english": "if" },
    { "id": 447, "tigrina": "እንተኾይና", "english": "if" },
    { "id": 448, "tigrina": "እንተኾነ", "english": "however" },
    { "id": 449, "tigrina": "እንተኮይነ", "english": "If I" },
    { "id": 450, "tigrina": "እንተኮይንካ", "english": "if you" },
    { "id": 451, "tigrina": "እንተኮይንኪ", "english": "if you" },
    { "id": 452, "tigrina": "እንተኮይንኩም", "english": "if you" },
    { "id": 453, "tigrina": "እንተኮይንክን", "english": "if you" },
    { "id": 454, "tigrina": "እንተኮይኑ", "english": "if" },
    { "id": 455, "tigrina": "እንተኮይና", "english": "if" },
    { "id": 456, "tigrina": "እንተኮይኖም", "english": "if they" },
    { "id": 457, "tigrina": "እንተኮይነን", "english": "if they are" },
    { "id": 458, "tigrina": "እንተኮይንና", "english": "if we" },
    { "id": 459, "tigrina": "እንተኾይነ", "english": "If I" },
    { "id": 460, "tigrina": "እንተኾይንካ", "english": "if you" },
    { "id": 461, "tigrina": "እንተኾይንኪ", "english": "if you" },
    { "id": 463, "tigrina": "እንተኾይንክን", "english": "if you" },
    { "id": 464, "tigrina": "እንተኾይኑ", "english": "if" },
    { "id": 465, "tigrina": "እንተኾይና", "english": "if" },
    { "id": 466, "tigrina": "እንተኾይኖም", "english": "if they" },
    { "id": 467, "tigrina": "እንተኾይነን", "english": "if they are" },
    { "id": 468, "tigrina": "እንተኾይንና", "english": "if we" },
    { "id": 445, "tigrina": "እንተኾኑ", "english": "if" },
    { "id": 446, "tigrina": "እንተኾና", "english": "if" },
    { "id": 447, "tigrina": "እንተኾይና", "english": "if" },
    { "id": 448, "tigrina": "እንተኾነ", "english": "however" },
    { "id": 449, "tigrina": "እንተኮይነ", "english": "If I" },
    { "id": 450, "tigrina": "እንተኮይንካ", "english": "if you" },
    { "id": 451, "tigrina": "እንተኮይንኪ", "english": "if you" },
    { "id": 452, "tigrina": "እንተኮይንኩም", "english": "if you" },
    { "id": 453, "tigrina": "እንተኮይንክን", "english": "if you" },
    { "id": 454, "tigrina": "እንተኮይኑ", "english": "if" },
    { "id": 455, "tigrina": "እንተኮይና", "english": "if" },
    { "id": 456, "tigrina": "እንተኮይኖም", "english": "if they" },
    { "id": 457, "tigrina": "እንተኮይነን", "english": "if they are" },
    { "id": 458, "tigrina": "እንተኮይንና", "english": "if we" },
    { "id": 459, "tigrina": "እንተኾይነ", "english": "If I" },
    { "id": 460, "tigrina": "እንተኾይንካ", "english": "if you" },
    { "id": 461, "tigrina": "እንተኾይንኪ", "english": "if you" },
    { "id": 462, "tigrina": "እንተኾይንኩም", "english": "if you" },
    { "id": 463, "tigrina": "እንተኾይንክን", "english": "if you" },
    { "id": 464, "tigrina": "እንተኾይኑ", "english": "if" },
    { "id": 465, "tigrina": "እንተኾይና", "english": "if" },
    { "id": 466, "tigrina": "እንተኾይኖም", "english": "if they" },
    { "id": 467, "tigrina": "እንተኾይነን", "english": "if they are" },
    { "id": 468, "tigrina": "እንተኾይንና", "english": "if we" },
    { "id": 469, "tigrina": "ካብዘይኮንኩ", "english": "since I'm not" },
    { "id": 470, "tigrina": "ካብዘይኮንካ", "english": "unless you" },
    { "id": 471, "tigrina": "ካብዘይኮንኪ", "english": "since you're not" },
    { "id": 472, "tigrina": "ካብዘይኮንኩም", "english": "unless you" },
    { "id": 473, "tigrina": "ካብዘይኮንክን", "english": "since you are not" },
    { "id": 474, "tigrina": "ካብዘይኮነ", "english": "from not" },
    { "id": 475, "tigrina": "ካብዘይኮነት", "english": "from not" },
    { "id": 476, "tigrina": "ካብዘይኮኑ", "english": "from those who are not" },
    { "id": 477, "tigrina": "ካብዘይኮና", "english": "since we are not" },
    { "id": 478, "tigrina": "ካብዘይኮንና", "english": "since we are not" },
    { "id": 479, "tigrina": "እንተዘይኮይነ", "english": "unless I" },
    { "id": 480, "tigrina": "እንተዘይኮይንካ", "english": "unless you" },
    { "id": 481, "tigrina": "እንተዘይኮይንኪ", "english": "andif you're not" },
    { "id": 482, "tigrina": "እንተዘይኮይንኩም", "english": "unless you" },
    { "id": 483, "tigrina": "እንተዘይኮይንክን", "english": "unless you" },
    { "id": 484, "tigrina": "እንተዘይኮይኑ", "english": "unless" },
    { "id": 485, "tigrina": "እንተዘይኮይና", "english": "unless" },
    { "id": 486, "tigrina": "እንተዘይኮይኖም", "english": "unless they" },
    { "id": 487, "tigrina": "እንተዘይኮይነን", "english": "unless" },
    { "id": 488, "tigrina": "እንተዘይኮይንና", "english": "unless we" },
    { "id": 489, "tigrina": "እንተዘይኮንኩ", "english": "unless I" },
    { "id": 490, "tigrina": "እንተዘይኮንካ", "english": "unless you" },
    { "id": 491, "tigrina": "እንተዘይኮንኪ", "english": "unless you" },
    { "id": 492, "tigrina": "እንተዘይኮንኩም", "english": "unless you" },
    { "id": 493, "tigrina": "እንተዘይኮንክን", "english": "if you're not" },
    { "id": 494, "tigrina": "እንተዘይኮነ", "english": "unless" },
    { "id": 495, "tigrina": "እንተዘይኮነት", "english": "unless" },
    { "id": 496, "tigrina": "እንተዘይኮኑ", "english": "unless" },
    { "id": 497, "tigrina": "እንተዘይኮና", "english": "unless" },
    { "id": 498, "tigrina": "እንተዘይኮንና", "english": "unless we" },
    { "id": 499, "tigrina": "ካብኮንኩ", "english": "since" },
    { "id": 500, "tigrina": "ካብኮንካ", "english": "since" },
    { "id": 501, "tigrina": "ካብኮንኪ", "english": "from" },
    { "id": 502, "tigrina": "ካብኮንኩም", "english": "if you" },
    { "id": 503, "tigrina": "ካብኮንክን", "english": "from" },
    { "id": 504, "tigrina": "ካብኮነ", "english": "if" },
    { "id": 505, "tigrina": "ካብኮነት", "english": "from" },
    { "id": 506, "tigrina": "ካብኮኑ", "english": "if" },
    { "id": 507, "tigrina": "ካብኮና", "english": "from us" },
    { "id": 508, "tigrina": "ካብኮንና", "english": "since" },
    { "id": 509, "tigrina": "ዘይምዃነይ", "english": "I am not" },
    { "id": 510, "tigrina": "ዘይምዃንካ", "english": "not being" },
    { "id": 511, "tigrina": "ዘይምዃንኪ", "english": "not being you" },
    { "id": 512, "tigrina": "ዘይምዃንኩም", "english": "you are not" },
    { "id": 513, "tigrina": "ዘይምዃንክን", "english": "not being" },
    { "id": 514, "tigrina": "ዘይምዃኑ", "english": "not being" },
    { "id": 515, "tigrina": "ዘይምዃና", "english": "not being" },
    { "id": 516, "tigrina": "ዘይምዃኖም", "english": "not being" },
    { "id": 517, "tigrina": "ዘይምዃነን", "english": "not being" },
    { "id": 518, "tigrina": "ዘይምዃና", "english": "not being" },
    { "id": 519, "tigrina": "ኮንኩ", "english": "I became" },
    { "id": 520, "tigrina": "ኮንካ", "english": "being" },
    { "id": 521, "tigrina": "ኮንኪ", "english": "Conki" },
    { "id": 522, "tigrina": "ኮንኩም", "english": "you" },
    { "id": 523, "tigrina": "ኮንክን", "english": "Konkan" },
    { "id": 524, "tigrina": "ኮነ", "english": "cone" },
    { "id": 525, "tigrina": "ኮነት", "english": "connected" },
    { "id": 526, "tigrina": "ኮኑ", "english": "become" },
    { "id": 527, "tigrina": "ኮና", "english": "we became" },
    { "id": 528, "tigrina": "ኮንና", "english": "we became" },
    { "id": 529, "tigrina": "ኮይነ", "english": "became" },
    { "id": 530, "tigrina": "ኮይንካ", "english": "being" },
    { "id": 531, "tigrina": "ኮይንኪ", "english": "being" },
    { "id": 532, "tigrina": "ኮይንኩም", "english": "being" },
    { "id": 533, "tigrina": "ኮይንክን", "english": "you" },
    { "id": 534, "tigrina": "ኮይኑ", "english": "became" },
    { "id": 535, "tigrina": "ኮይና", "english": "became" },
    { "id": 536, "tigrina": "ኮይኖም", "english": "being" },
    { "id": 537, "tigrina": "ኮይነን", "english": "became" },
    { "id": 538, "tigrina": "ኮይንና", "english": "became" },
    { "id": 539, "tigrina": "ከይኮንኩ", "english": "without being" },
    { "id": 540, "tigrina": "ከይኮንካ", "english": "without being" },
    { "id": 541, "tigrina": "ከይኮንኪ", "english": "without being" },
    { "id": 542, "tigrina": "ከይኮንኩም", "english": "without being" },
    { "id": 543, "tigrina": "ከይኮንክን", "english": "without you" },
    { "id": 544, "tigrina": "ከይኮነ", "english": "without being" },
    { "id": 469, "tigrina": "ካብዘይኮንኩ", "english": "since I'm not" },
    { "id": 470, "tigrina": "ካብዘይኮንካ", "english": "unless you" },
    { "id": 471, "tigrina": "ካብዘይኮንኪ", "english": "since you're not" },
    { "id": 472, "tigrina": "ካብዘይኮንኩም", "english": "unless you" },
    { "id": 473, "tigrina": "ካብዘይኮንክን", "english": "since you are not" },
    { "id": 474, "tigrina": "ካብዘይኮነ", "english": "from not" },
    { "id": 475, "tigrina": "ካብዘይኮነት", "english": "from not" },
    { "id": 476, "tigrina": "ካብዘይኮኑ", "english": "from those who are not" },
    { "id": 477, "tigrina": "ካብዘይኮና", "english": "since we are not" },
    { "id": 478, "tigrina": "ካብዘይኮንና", "english": "since we are not" },
    { "id": 479, "tigrina": "እንተዘይኮይነ", "english": "unless I" },
    { "id": 480, "tigrina": "እንተዘይኮይንካ", "english": "unless you" },
    { "id": 481, "tigrina": "እንተዘይኮይንኪ", "english": "andif you're not" },
    { "id": 482, "tigrina": "እንተዘይኮይንኩም", "english": "unless you" },
    { "id": 483, "tigrina": "እንተዘይኮይንክን", "english": "unless you" },
    { "id": 484, "tigrina": "እንተዘይኮይኑ", "english": "unless" },
    { "id": 485, "tigrina": "እንተዘይኮይና", "english": "unless" },
    { "id": 486, "tigrina": "እንተዘይኮይኖም", "english": "unless they" },
    { "id": 487, "tigrina": "እንተዘይኮይነን", "english": "unless" },
    { "id": 488, "tigrina": "እንተዘይኮይንና", "english": "unless we" },
    { "id": 489, "tigrina": "እንተዘይኮንኩ", "english": "unless I" },
    { "id": 490, "tigrina": "እንተዘይኮንካ", "english": "unless you" },
    { "id": 491, "tigrina": "እንተዘይኮንኪ", "english": "unless you" },
    { "id": 492, "tigrina": "እንተዘይኮንኩም", "english": "unless you" },
    { "id": 493, "tigrina": "እንተዘይኮንክን", "english": "if you're not" },
    { "id": 494, "tigrina": "እንተዘይኮነ", "english": "unless" },
    { "id": 495, "tigrina": "እንተዘይኮነት", "english": "unless" },
    { "id": 496, "tigrina": "እንተዘይኮኑ", "english": "unless" },
    { "id": 497, "tigrina": "እንተዘይኮና", "english": "unless" },
    { "id": 498, "tigrina": "እንተዘይኮንና", "english": "unless we" },
    { "id": 499, "tigrina": "ካብኮንኩ", "english": "since" },
    { "id": 500, "tigrina": "ካብኮንካ", "english": "since" },
    { "id": 501, "tigrina": "ካብኮንኪ", "english": "from" },
    { "id": 502, "tigrina": "ካብኮንኩም", "english": "if you" },
    { "id": 503, "tigrina": "ካብኮንክን", "english": "from" },
    { "id": 504, "tigrina": "ካብኮነ", "english": "if" },
    { "id": 505, "tigrina": "ካብኮነት", "english": "from" },
    { "id": 506, "tigrina": "ካብኮኑ", "english": "if" },
    { "id": 507, "tigrina": "ካብኮና", "english": "from us" },
    { "id": 508, "tigrina": "ካብኮንና", "english": "since" },
    { "id": 509, "tigrina": "ዘይምዃነይ", "english": "I am not" },
    { "id": 510, "tigrina": "ዘይምዃንካ", "english": "not being" },
    { "id": 511, "tigrina": "ዘይምዃንኪ", "english": "not being you" },
    { "id": 512, "tigrina": "ዘይምዃንኩም", "english": "you are not" },
    { "id": 513, "tigrina": "ዘይምዃንክን", "english": "not being" },
    { "id": 514, "tigrina": "ዘይምዃኑ", "english": "not being" },
    { "id": 515, "tigrina": "ዘይምዃና", "english": "not being" },
    { "id": 516, "tigrina": "ዘይምዃኖም", "english": "not being" },
    { "id": 517, "tigrina": "ዘይምዃነን", "english": "not being" },
    { "id": 518, "tigrina": "ዘይምዃና", "english": "not being" },
    { "id": 519, "tigrina": "ኮንኩ", "english": "I became" },
    { "id": 520, "tigrina": "ኮንካ", "english": "being" },
    { "id": 521, "tigrina": "ኮንኪ", "english": "Conki" },
    { "id": 522, "tigrina": "ኮንኩም", "english": "you" },
    { "id": 523, "tigrina": "ኮንክን", "english": "Konkan" },
    { "id": 524, "tigrina": "ኮነ", "english": "cone" },
    { "id": 525, "tigrina": "ኮነት", "english": "connected" },
    { "id": 526, "tigrina": "ኮኑ", "english": "become" },
    { "id": 527, "tigrina": "ኮና", "english": "we became" },
    { "id": 528, "tigrina": "ኮንና", "english": "we became" },
    { "id": 529, "tigrina": "ኮይነ", "english": "became" },
    { "id": 530, "tigrina": "ኮይንካ", "english": "being" },
    { "id": 531, "tigrina": "ኮይንኪ", "english": "being" },
    { "id": 532, "tigrina": "ኮይንኩም", "english": "being" },
    { "id": 533, "tigrina": "ኮይንክን", "english": "you" },
    { "id": 534, "tigrina": "ኮይኑ", "english": "became" },
    { "id": 535, "tigrina": "ኮይና", "english": "became" },
    { "id": 536, "tigrina": "ኮይኖም", "english": "being" },
    { "id": 537, "tigrina": "ኮይነን", "english": "became" },
    { "id": 538, "tigrina": "ኮይንና", "english": "became" },
    { "id": 539, "tigrina": "ከይኮንኩ", "english": "without being" },
    { "id": 540, "tigrina": "ከይኮንካ", "english": "without being" },
    { "id": 541, "tigrina": "ከይኮንኪ", "english": "without being" },
    { "id": 542, "tigrina": "ከይኮንኩም", "english": "without being" },
    { "id": 543, "tigrina": "ከይኮንክን", "english": "without you" },
    { "id": 544, "tigrina": "ከይኮነ", "english": "without being" },
    { "id": 545, "tigrina": "ከይኮነት", "english": "without being" },
    { "id": 546, "tigrina": "ከይኮኑ", "english": "not to be" },
    { "id": 547, "tigrina": "ከይኮና", "english": "not to be" },
    { "id": 548, "tigrina": "ከይኮንና", "english": "without being" },
    { "id": 549, "tigrina": "ዘይከኣልኩ", "english": "unable" },
    { "id": 550, "tigrina": "ዘይከኣልካ", "english": "you can't" },
    { "id": 551, "tigrina": "ዘይከኣልኪ", "english": "you couldn't" },
    { "id": 552, "tigrina": "ዘይከኣልኩም", "english": "you couldn't" },
    { "id": 553, "tigrina": "ዘይከኣልክን", "english": "you couldn't" },
    { "id": 554, "tigrina": "ዘይከኣለ", "english": "unable" },
    { "id": 555, "tigrina": "ዘይከኣለት", "english": "unable" },
    { "id": 556, "tigrina": "ዘይከኣሉ", "english": "impossible" },
    { "id": 557, "tigrina": "ዘይከኣላ", "english": "unable" },
    { "id": 558, "tigrina": "ዘይከኣልና", "english": "we couldn't" },
    { "id": 559, "tigrina": "ከኣልኩ", "english": "I could" },
    { "id": 560, "tigrina": "ከኣልካ", "english": "you could" },
    { "id": 561, "tigrina": "ከኣልኪ", "english": "you could" },
    { "id": 562, "tigrina": "ከኣልኩም", "english": "you could" },
    { "id": 563, "tigrina": "ከኣልክን", "english": "you could" },
    { "id": 564, "tigrina": "ከኣለ", "english": "could" },
    { "id": 565, "tigrina": "ከኣለት", "english": "could" },
    { "id": 566, "tigrina": "ከኣሉ", "english": "could" },
    { "id": 567, "tigrina": "ከኣላ", "english": "capable" },
    { "id": 568, "tigrina": "ከኣልና", "english": "we could" },
    { "id": 569, "tigrina": "ዘይምኽኣለይ", "english": "my inability" },
    { "id": 570, "tigrina": "ዘይምኽኣልካ", "english": "your inability" },
    { "id": 571, "tigrina": "ዘይምኽኣልኪ", "english": "your inability" },
    { "id": 572, "tigrina": "ዘይምኽኣልኩም", "english": "your inability" },
    { "id": 573, "tigrina": "ዘይምኽኣልክን", "english": "your inability" },
    { "id": 574, "tigrina": "ዘይምኽኣሉ", "english": "his inability" },
    { "id": 575, "tigrina": "ዘይምኽኣላ", "english": "her inability" },
    { "id": 576, "tigrina": "ዘይምኽኣሎም", "english": "their inability" },
    { "id": 577, "tigrina": "ዘይምኽኣለን", "english": "their inability" },
    { "id": 578, "tigrina": "ዘይምኽኣልና", "english": "our inability" },
    { "id": 579, "tigrina": "ዘይምኽኣል", "english": "inability" },
    { "id": 580, "tigrina": "ዘይክእል", "english": "unable" },
    { "id": 581, "tigrina": "ዘይትኽእል", "english": "unable" },
    { "id": 582, "tigrina": "ዘይትኽእሊ", "english": "unable" },
    { "id": 583, "tigrina": "ዘይትኽእሉ", "english": "you can't" },
    { "id": 584, "tigrina": "ዘይትኽእላ", "english": "unable" },
    { "id": 585, "tigrina": "ዘይክእል", "english": "unable" },
    { "id": 586, "tigrina": "ዘይትኽእል", "english": "unable" },
    { "id": 587, "tigrina": "ዘይኽእሉ", "english": "unable" },
    { "id": 588, "tigrina": "ዘይክእላ", "english": "unable" },
    { "id": 589, "tigrina": "ዘይንኽእል", "english": "we can't" },
    { "id": 590, "tigrina": "ከይከኣልኩ", "english": "unable" },
    { "id": 591, "tigrina": "ከይክኣልካ", "english": "without being able" },
    { "id": 592, "tigrina": "ከይክኣልኪ", "english": "If you can" },
    { "id": 593, "tigrina": "ከይክኣልኩም", "english": "unable" },
    { "id": 594, "tigrina": "ከይክኣልክን", "english": "you can't" },
    { "id": 595, "tigrina": "ከይክኣለ", "english": "unable" },
    { "id": 596, "tigrina": "ከይክኣለት", "english": "couldn't" },
    { "id": 597, "tigrina": "ከይክኣሉ", "english": "unable" },
    { "id": 598, "tigrina": "ከይክኣላ", "english": "unable" },
    { "id": 599, "tigrina": "ከይክኣልና", "english": "we cannot" },
    { "id": 600, "tigrina": "ከይከኣልኩ ከለኹ", "english": "when I can't" },
    { "id": 601, "tigrina": "ከይክኣልካ ከለኻ", "english": "when you can't" },
    { "id": 602, "tigrina": "ከይክኣልኪ ከለኺ", "english": "when you can't" },
    { "id": 603, "tigrina": "ከይክኣልኩም ከለኹም", "english": "when you can't" },
    { "id": 604, "tigrina": "ከይክኣልክን ከለኽን", "english": "when you can't" },
    { "id": 605, "tigrina": "ከይክኣለ ከሎ", "english": "when he cannot" },
    { "id": 606, "tigrina": "ከይክኣለት ከላ", "english": "when she couldn't" },
    { "id": 607, "tigrina": "ከይክኣሉ ከለዉ", "english": "when they can't" },
    { "id": 608, "tigrina": "ከይክኣላ ከለዋ", "english": "when they can't" },
    { "id": 609, "tigrina": "ከይክኣልና ከለና", "english": "when we can't" },
    { "id": 610, "tigrina": "ጸኒሐ", "english": "later" },
    { "id": 611, "tigrina": "ጸኒሕካ", "english": "later" },
    { "id": 612, "tigrina": "ጸኒሕኪ", "english": "you stayed" },
    { "id": 613, "tigrina": "ጸኒሕኩም", "english": "later" },
    { "id": 614, "tigrina": "ጸኒሕክን", "english": "you stayed" },
    { "id": 615, "tigrina": "ጸኒሑ", "english": "later" },
    { "id": 616, "tigrina": "ጸኒሓ", "english": "later" },
    { "id": 617, "tigrina": "ጸኒሖም", "english": "later" },
    { "id": 618, "tigrina": "ጸኒሐን", "english": "later" },
    { "id": 619, "tigrina": "ጸኒሕና", "english": "we stayed" },
    { "id": 620, "tigrina": "ኣይጸናሕኩን", "english": "I didn't stay" },
    { "id": 621, "tigrina": "ኣይጸናሕካን", "english": "you didn't stay" },
    { "id": 622, "tigrina": "ኣይጸናሕክን", "english": "You didn't stay" },
    { "id": 623, "tigrina": "ኣይጸናሕኩምን", "english": "you didn't stay" },
    { "id": 624, "tigrina": "ኣይጸናሕክንን", "english": "I didn't stay" },
    { "id": 625, "tigrina": "ኣይጸንሐን", "english": "didn't last" },
    { "id": 626, "tigrina": "ኣይጸነሐትን", "english": "She didn't stay" },
    { "id": 627, "tigrina": "ኣይጸንሑን", "english": "they don't last" },
    { "id": 628, "tigrina": "ኣይጸንሓን", "english": "It didn't last" },
    { "id": 629, "tigrina": "ኣይጸናሕናን", "english": "we didn't stay" },
    { "id": 630, "tigrina": "ነበርኩ", "english": "I was" },
    { "id": 631, "tigrina": "ነበርካ", "english": "you were" },
    { "id": 632, "tigrina": "ነበርኪ", "english": "you were" },
    { "id": 633, "tigrina": "ነበርኩም", "english": "were" },
    { "id": 634, "tigrina": "ነበርክን", "english": "you were" },
    { "id": 635, "tigrina": "ነበረ", "english": "was" },
    { "id": 636, "tigrina": "ነበረት", "english": "was" },
    { "id": 637, "tigrina": "ነበሩ", "english": "were" },
    { "id": 638, "tigrina": "ነበራ", "english": "was" },
    { "id": 639, "tigrina": "ነበርና", "english": "we were" }
]
statments_and_questions_verb_to_be=[]
def pronouns(text):
    info = {}
    if text in ['ንስኻ', 'ንስኺ', 'ንስኹም', 'ንስኽን', 'ንስኻትኩም', 'ንስኻትክን']:
        info['pronoun'] = 'you'
    elif text == 'ንሱ':
        info['pronoun'] = 'he'
    elif text == 'ንሳ':
        info['pronoun'] = 'she'
    elif text in ['ንሶም', 'ንሰን', 'ንሳቶም', 'ንሳተን']:
        info['pronoun'] = 'they'
    elif text == 'ኣነ':
        info['pronoun'] = 'i'
    elif text == 'ንሕና':
        info['pronoun'] = 'we'
    else:
        info['pronoun'] = ''
    return info
def verb_to_be_past_tense_or_present_checker(text):
    info = {}
    if text == 'ኢየ':
        info['verbToBe'] = 'am'
    elif text in ['ኢኻ', 'ኢኺ', 'ኢኹም', 'ኢኽን', 'ኢዮም', 'ኢየን', 'ኢና']:
        info['verbToBe'] = 'are'
    elif text in ['ኢያ', 'ኢዩ']:
        info['verbToBe'] = 'is'
    else:
        info['verbToBe'] = ''
    return info
def verb_to_be_pastence_or_present_checker(text):
    info = {}

    if text == 'ኢየ':
        info['verbToBe'] = "am"
    elif text in ['ኢኻ', 'ኢኺ', 'ኢኹም', 'ኢኽን', 'ኢዮም', 'ኢየን', 'ኢና']:
        info['verbToBe'] = "are"
    elif text in ['ኢያ', 'ኢዩ']:
        info['verbToBe'] = "is"
    else:
        info['verbToBe'] = ""

    return info
def find_pronoun_from_verb_to_be(text,index):
    aneCollection=[
    'ነይሩኒ','ነሩኒ','ነይረ','ነረ','ኔሩኒ','ዲየ','እንተኮይነ','ዘይምዃነይ','እንተዘይኮንኩ','እንተዘይኮይነ','ዘይኮንኩ','ካብኮንኩ','ካብዘይኮንኩ','ዘይኮንኩ','ከይከኣልኩ','ዘይክእል','ዘይምኽኣለይ','ከኣልኩ','ዘይከኣልኩ','ከይኮንኩ', 'ኮንኩ','ኮይነ','እንተኾይነ','ከምዝክእል','ከምዝኽእል','ከምዘይክእል','ከምዘይኽእል','ምኻኣልኩ','ነበርኩ','ኣይጸናሕኩን','ጸኒሐ','ኔሮሙኒ','ኔሮምኒ','ኣለዉኒ','ኣለውኒ','ኣይነበርኩን','ኣይክኸውንን','ክኸውን','ድኸውን','ዝኸውን','ይኸውን','ይኽእል','ኣይክህልወንን','ክህልወኒ','የብለይን','ኣይኸውንን','ኣይምኾንኩን','ኣይክእልን','ኣይከውንን','ኣይነበረካን','ኣይነበረንን','ኣይኮንኩን','ኣለኹ','ምኾንኩ','ድየ','ከለኹ','ዝነበርኩ','ዘለኹ','ምኽኣልኩ','ኣይምኽኣልኩን','ኢየ','ኔረ','ኣለኒ','ኔሩኒ','ኔርኒ']
    nsKaCollection=[
    'ነይሩካ','ነሩካ','ነይርካ','ነርካ','ኔሩካ','ድኻ','እንተኮይንካ','ዘይምዃንካ','እንተዘይኮንካ','እንተዘይኮይንካ','ዘይኮንካ','ካብኮንካ','ካብዘይኮንካ','ዘይኮንካ','ከይክኣልካ','ዘይትኽእል','ዘይምኽኣልካ','ከኣልካ','ዘይከኣልካ','ከይኮንካ','ኮንካ','ኮይንካ','እንተኾይንካ', 'ከምዘይትኽእል','ከምትክእል','ከምትኽእል','ምኻኣልካ','ነበርካ','ኣይጸናሕካን','ጸኒሕካ','ኔሮሙኻ','ኔሮምኻ','ኣለዉኻ','ኣለውኻ','ኣይነበርካን','ክትከውን','ኣይክህልወካን','ክህልወካ','የብልካን','ኣይምኾንካን','ኣይትኽእልን','ኣይክትከውንን','ኣይኮንካን','ኣለካ','ምኾንካ','ዲኻ','ከለኻ','ዝነበርካ','ዘለኻ','ምኽኣልካ','ኣይምኽኣልካን','ኢኻ','ኔርካ','ኣለኻ','ኔርካ']
    nsKiCollection=[
    'ነይሩኪ','ነሩኪ','ነይርኪ','ነርኪ','ኔሩኪ','ድኺ','እንተኮይንኪ','ዘይምዃንኪ','እንተዘይኮንኪ','እንተዘይኮይንኪ','ዘይኮንኪ','ካብኮንኪ','ካብዘይኮንኪ','ዘይኮንኪ','ከይክኣልኪ','ዘይትኽእሊ','ዘይምኽኣልኪ','ከኣልኪ','ዘይከኣልኪ','ከይኮንኪ','ኮንኪ','ኮይንኪ','እንተኾይንኪ','ከምዘይትክእሊ','ከምዘይትኽእሊ','ከምትክእሊ','ከምትኽእሊ','ምኻኣልኪ','ነበርኪ','ኣይጸናሕክን','ጸኒሕኪ','ኔሮሙኺ','ኔሮምኺ','ኣለዉኺ','ኣለውኺ','ኣይነበርክን','ክትኮኒ','ትኽእላ','ኣይክህልወኪን','ክህልወኪ','የብልክን','ኣይምኾንኪን','ኣይትኽእልን','ኣይክትኮንን','ኣይነበረክን','ኣይኮንክን','ኣለኺ','ምኾንኪ','ዲኺ','ከለኺ','ዝነበርኪ','ዘለኺ','ምኽኣልኪ','ኣይምኽኣልክን','ከለኺ','ኢኺ','ኔርኪ','ኣለኪ','ኔርኪ','ዘለኪ']
    nsKumCollection=[
    'ነይሩኩም','ነሩኩም','ነይርኩም','ነርኩም','ኔሩኩም','ድኹም','እንተኮይንኩም','ዘይምዃንኩም','እንተዘይኮንኩም','እንተዘይኮይንኩም','ዘይኮንኩም','ካብኮንኩም','ካብዘይኮንኩም','ዘይኮንኩም','ከይክኣልኩም','ዘይትኽእሉ','ዘይምኽኣልኩም','ከኣልኩም','ዘይከኣልኩም','ከይኮንኩም','ኮንኩም','ኮይንኩም','እንተኾይንኩም','ከምዘይትክእሉ','ከምዘይትኽእሉ','ከምትክእሉ','ከምትኽእሉ','ምኻኣልኩም','ነበርኩም','ኣይጸናሕኩምን','ጸኒሕኩም','ኔሮሙኹም','ኔሮምኹም','ኣለዉኹም','ኣለውኹም','ኣይነበርኩምን','ክትኮኑ','ትኾኑ','ትኽእሉ','ኣይክህልወኩምን','ክህልወኩም','የብልኩምን','ኣይትኾኑን','ኣይምኾንኩምን','ኣይትኽእሉን','ኣይክትኮኑን','ኣይነበርኩምን','ኣይኮንኩምን','ኣለኩም','ምኾንኩም','ዲኹም','ከለኹም','ዝነበርኩም','ዘለኹም','ምኽኣልኩም','ኣይምኽኣልኩምን','ዲኹም','ከለኹም','ኢኹም','ኔርኩም','ኣለኹም','ኔርኩም','ዘለኹም','ዘለኩም']
    nsKnCollection=[
    'ነይሩክን','ነሩክን','ነይርክን','ነርክን','ኔሩክን','ድኽን','እንተኮይንክን','ዘይምዃንክን','እንተዘይኮንክን','እንተዘይኮይንክን','ዘይኮንክን','ካብኮንክን','ካብዘይኮንክን','ዘይኮንክን','ከይክኣልክን','ዘይትኽእላ','ዘይምኽኣልክን','ከኣልክን','ዘይከኣልክን','ከይኮንክን','ኮንክን','ኮይንክን','እንተኾይንክን','ከምዘይትክእላ','ከምዘይትኽእላ','ከምትክእላ','ከምትኽእላ','ምኻኣልክን','ነበርክን','ኣይጸናሕክንን','ጸኒሕክን','ኔሮሙኽን','ኔሮምኽን','ለዉኽን','ኣለውኽን','ኣይነበርክን','ክትኮና','ትኾና','ኣይክህልወክንን','ክህልወክን','የብልክንን','ኣይትኾናን','ኣይምኾንክንን','ኣይትኽእላን','ኣይክትኮናን','ኣይነበረክንን','ኣይኮንክንን','ኣለክን','ምኾንክን','ዲኽን','ከለኽን','ከለክን','ዝነበርክን','ዘለኽን','ምኽኣልክን','ኣይምኽኣልክንን','ዲኽን','ከለኽን','ኢኽን','ኔርክን','ዘለክን','ዘለኽን']
    nsuCollection=[
    'ነይሩዎ','ነሩዎ','ነይሩ','ነሩ','ኔሩዎ','ዲዩ','እንተኮይኑ','ዘይምዃኑ','እንተዘይኮነ','እንተዘይኮይኑ','ዘይኮነ','ካብኮነ', 'ካብዘይኮነ','ዘይኮነ','ከይክኣለ','ዘይክእል','ዘይምኽኣሉ','ከኣለ','ዘይከኣለ','ከይኮነ','ኮነ','ኮይኑ','እንተኾይኑ','ከምዘይኽእል','ከምዝክእል','ምኻኣለ','ነበረ','ኣይጸንሐን','ኣይጸንሐን','ጸኒሑ','ኔሮሞ','ኣለዉዎ','ኣለውዎ','ኣይነበረን','ኣይክኸውንን','ክኸውን','ድኸውን','ዝኸውን','ይኸውን','ይኽእል','ኣይክህልዎን','ክህልዎ','የብሉን','ኣይኸውንን','ኣይምኾነን','ኣይክእልን','ኣይከውንን','ኣይነበሮን','ኣይኮነን','ኣሎ','ምኾነ','ድዩ','ከሎ','ዝነበረ','ዘሎ','ምኽኣለ','ኣይምኽኣለን','ድዩ','ከሎ','ኢዩ','ኔሩ','ኣለዎ','ኔርዎ','ዘሎ']
    nsaCollection=[
    'ነይሩዋ','ነሩዋ','ነይራ','ነራ','ኔሩዋ','ዲያ','እንተኮይና','ዘይምዃና','እንተዘይኮነት','እንተዘይኮይና','ዘይኮነት', 'ካብኮነት','ካብዘይኮነት','ዘይኮነት','ከይክኣለት','ዘይትኽእል','ዘይምኽኣላ','ከኣለት','ዘይከኣለት','ከይኮነት','ኮነት','ኮይና','እንተኾይና','ከምዘይትኽእል','ከምትክእል','ከምትኽእል','ምኻኣለት','ነበረት','ኣይጸነሐትን','ኣይጸነሐትን','ጸኒሓ','ኔሮማ','ኣለዉዋ','ኣለውዋ','ኣይነበረትን','ትኸውን','ትኽእል','ኣይክህልዋን','ክህልዋ','የብላን','ኣይትኸውንን','ኣይምኾነትን','ኣይትኽእልን','ኣይክትከውንን','ኣይነበራን','ኣይኮነትን','ኣላ','ምኾነት','ድያ','ከላ','ዝነበረት','ዘላ','ምኽኣለት','ኣይምኽኣለትን','ድያ','ኢያ','ኔራ','ኣለዋ','ኔርዋ','ዘላ']
    nsomCollection=[
    'ነይሩዎም','ነሩዎም','ነይሮም','ነሮም','ኔሩዎም','ዲዮም','እንተኮይኖም','ዘይምዃኖም','እንተዘይኮኑ','እንተዘይኮይኖም','ዘይኮኑ','ካብኮኑ','ካብዘይኮኑ','ዘይኮኑ','ከይክኣሉ','ዘይኽእሉ','ዘይምኽኣሎም','ከኣሉ','ዘይከኣሉ','ከይኮኑ','ኮኑ','ኮይኖም', 'እንተኾይኖም','ከምዘይክእሉ','ከምዘይኽእሉ','ከምዝክእሉ','ከምዝኽእሉ','ምኻኣሉ','ነበሩ','ኣይጸንሑን','ጸኒሖም','ኔሮሞም','ኣለዉዎም','ኣለውዎም','ኣይነበሩን','ክኾኑ','ድኾኑ','ዝኾኑ','ይኾኑ','ይኽእሉ','ኣይክህልዎምን','ክህልዎም','የብሎምን','ኣይኾኑን','ኣይምኾኑን','ኣይክእሉን','ኣይነበሮምን','ኣይኮኑን','ኣለዉ','ምኾኑ','ድዮም','ከለዉ','ዝነበሩ','ዘለዉ','ምኽኣሉ','ኣይምኽኣሉን','ከለዉ','ኢዮም','ኔሮም','ኣለዎም','ኔርዎም','ዘለዉ']
    nsenCollection=[
    'ነይሩወን','ነሩወን','ነይረን','ነረን','ኔሩወን','ዲየን','እንተኮይነን','ዘይምዃነን', 'እንተዘይኮና','እንተዘይኮይነን','ዘይኮና','ካብኮና','ካብዘይኮና','ዘይኮና','ከይክኣላ','ዘይክእላ','ዘይምኽኣለን','ከኣላ','ዘይከኣላ','ከይኮና','ኮና','ኮይነን','እንተኾይነን','ከምዘይክእላ','ከምዘይኽእላ','ከምዝክእላ','ከምዝኽእላ','ምኻኣላ','ነበራ','ኣይጸንሓን','ጸኒሐን','ኔሮመን','ኣለውዎም','ኣለዉወን','ኣይነበራን','ክኾና','ድኾና','ዝኾና','ይኾና','ይኽእላ','ኣይክህልወንን','ክህልወን','የብለንን','ኣይኾናን','ኣይምኾናን','ኣይክእላን','ኣይክኾናን','ኣይነበረንን','ኣይኮናን','ኣለዋ','ምኾና','ድየን','ከለዋ','ዝነበራ','ዘለዋ','ምኽኣላ','ኣይምኽኣላን','ድየን','ከለዋ','ኢየን','ኔረን','ኣለወን','ኔርወን','ዘለዋ']
    nhnaCollection=[
    'ነይሩና','ነሩና','ነይርና','ነርና','ኔሩና','ድና','እንተኮይንና','ዘይምዃና','እንተዘይኮንና','እንተዘይኮይንና','ዘይኮንና','ካብኮንና','ካብዘይኮንና','ዘይኮንና','ከይክኣልና','ዘይንኽእል','ዘይምኽኣልና','ከኣልና','ዘይከኣልና','ከይኮንና','ኮንና','ኮይንና','እንተኾይንና','ከምዘይንክእል','ከምዘይንኽእል','ከምንክእል', 'ከምንኽእል','ምኻኣልና','ነበርና','ኣይጸናሕናን','ጸኒሕና','ኔሮሙና','ኔሮምና','ኣለዉና','ኣለውና','ኣይነበርናን','ንኸውን','ንኽእል','ኣይክህልወናን','ክህልወና','የብልናን','ኣይንኸውንን','ኣይምኾንናን','ኣይንኽእልን','ኣይክንከውንን','ኣይነበረናን','ኣይኮንናን','ኣለና','ምኾንና','ዲና','ከለና','ዝነበርና','ዘለና','ምኽኣልና','ኣይምኽኣልናን','ዲና','ኸለና','ኢና','ኔርና','ኣለና','ኔርና','ኔሩና','ዘለና']
    info = {}
    if text in aneCollection:
        info['text'] = 'ane'
        info['index'] = index
        info['english'] = 'i'
        t_sentence_pronoun.append(info)
    elif text in nsKaCollection:
        info['text'] = 'nisika'
        info['index'] = index
        info['english'] = 'you'
        t_sentence_pronoun.append(info)
    elif text in nsKiCollection:
        info['text'] = 'nsKi'
        info['index'] = index
        info['english'] = 'you'
        t_sentence_pronoun.append(info)
    elif text in nsKumCollection:
        info['text'] = 'nsKum'
        info['index'] = index
        info['english'] = 'you'
        t_sentence_pronoun.append(info)
    elif text in nsKnCollection:
        info['text'] = 'nsKn'
        info['index'] = index
        info['english'] = 'you'
        t_sentence_pronoun.append(info)
    elif text in nsuCollection:
        info['text'] = 'nsu'
        info['index'] = index
        info['english'] = 'he'
        t_sentence_pronoun.append(info)
    elif text in nsaCollection:
        info['text'] = 'nsa'
        info['index'] = index
        info['english'] = 'she'
        t_sentence_pronoun.append(info)
    elif text in nsomCollection:
        info['text'] = 'nsom'
        info['index'] = index
        info['english'] = 'they'
        t_sentence_pronoun.append(info)
    elif text in nsenCollection:
        info['text'] = 'nsen'
        info['index'] = index
        info['english'] = 'they'
        t_sentence_pronoun.append(info)
    elif text in nhnaCollection:
        info['text'] = 'nhna'
        info['index'] = index
        info['english'] = 'we'
        t_sentence_pronoun.append(info)

    return info

def whes_english(text):
    info = {}
    if text in ['ኣበይ', 'ናበይ', 'ካበይ']:
        info['english'] = 'where'
    elif text in ['በየን', 'በየናይ', 'በበይ']:
        info['english'] = 'from which direction'
    elif text == 'መዓስ':
        info['english'] = 'when'
    elif text == 'ንመን':
        info['english'] = 'to whom'
    elif text == 'እንታይ':
        info['english'] = 'what'
    elif text in ['kemey', 'ከመይ']:
        info['english'] = 'how'
    elif text in ['ብኸመይ', 'ብከመይ']:
        info['english'] = 'how'
    elif text == 'መን':
        info['english'] = 'who'
    elif text == 'ክንደይ':
        info['english'] = 'how many'
    elif text == 'ኣየናይ':
        info['english'] = 'which'
    elif text == 'ናበየናይ':
        info['english'] = 'to which'
    elif text == 'ስለምንታይ':
        info['english'] = 'why'
    elif text == 'ክንደይ ዝኸውን':
        info['english'] = 'how much'
    elif text == 'ምስ መን':
        info['english'] = 'with whom'
    elif text == 'መበል ክንደይ':
        info['english'] = 'how much of it'
    
    return info

def tigrina_indicators(text):
    info = {}
    if text == 'እቲ':
        info['english'] = 'the'
    elif text == 'እዚ':
        info['english'] = 'this'
    elif text == 'እቲኦም':
        info['english'] = 'those'
    elif text == 'እቶም':
        info['english'] = 'the'
    elif text == 'እዚኦም':
        info['english'] = 'these are'
    elif text == 'እቲኤን':
        info['english'] = 'these'
    elif text == 'እተን':
        info['english'] = 'the'
    elif text == 'እዚኤን':
        info['english'] = 'these are'
    elif text == 'እዘን':
        info['english'] = 'these'
    elif text == 'እቲኣቶም':
        info['english'] = 'those are the ones'
    elif text == 'እቲኣተን':
        info['english'] = 'those are the ones'
    elif text == 'እዚኣቶም':
        info['english'] = 'these are the ones'
    elif text == 'እዞም':
        info['english'] = 'these'
    elif text == 'ነቲ':
        info['english'] = 'the one'
    elif text == 'ነቶም':
        info['english'] = 'for those who'
    elif text == 'ነተን':
        info['english'] = 'for those who'
    elif text == 'ነታ':
        info['english'] = 'for those who'
    elif text == 'ነቲኦም':
        info['english'] = 'to those of them'
    elif text == 'ነቲአን':
        info['english'] = 'to those of them'
    elif text == 'ነቲኣ':
        info['english'] = 'that one'
    elif text == 'ነቲኣተን':
        info['english'] = 'the ones that'
    elif text == 'ነቲኣቶም':
        info['english'] = 'the ones that'
    return info

def tigrina_possesses(text):
    info = {}
    if text == 'ናተይ':
        info['english'] = 'mine'
    elif text in ['ናትካ', 'ናትኪ', 'ናትኩም', 'ናትክን']:
        info['english'] = 'yours'
    elif text == 'ናቱ':
        info['english'] = 'his'
    elif text == 'ናታ':
        info['english'] = 'hers'
    elif text in ['ናቶም', 'ናተን']:
        info['english'] = 'their'
    elif text in ['ናትና', 'ናታትና']:
        info['english'] = 'ours'
    elif text in ['ናታትኩም', 'ናታትክን']:
        info['english'] = 'yours'
    elif text in ['ናታቶም', 'ናታተን']:
        info['english'] = 'theirs'
    elif text in ['ናዓይ', 'ንዓይ']:
        info['english'] = 'to me'
    elif text in ['ናዓኻ', 'ንዓኻ']:
        info['english'] = 'to you'
    elif text in ['ናዓኺ', 'ንዓኺ']:
        info['english'] = 'to you'
    elif text in ['ናዓኹም', 'ንዓኹም']:
        info['english'] = 'to you'
    elif text in ['ናዓኽን', 'ንዓኽን']:
        info['english'] = 'to you'
    elif text == 'ንዕኡ':
        info['english'] = 'to him'
    elif text in ['ንዓኣ', 'ናዓኣ']:
        info['english'] = 'to her'
    elif text == 'ንዕኦም':
        info['english'] = 'to them'
    elif text == 'ንዕአን':
        info['english'] = 'to them'
    elif text in ['ናዓና', 'ንዓና']:
        info['english'] = 'to us'
    return info
tigrina_pronoun_collection=[]
t_sentence_excludes=[]
def fabricate(text):
    global possess
    t_sentence_array = text.split(' ')
    for index, item in enumerate(t_sentence_array):
        verbToBeExcludes = []
        verbtobeInfo = {}
        if item in tigrina_pronoun:
            englishPronoun = pronouns(item)
            tigrina_pronoun_collection.append({'pronoun': englishPronoun['pronoun'], 'index': index, 'type': 'pronoun'})
        elif item in possess:
            info = {}
            possess = tigrina_possesses(item)
            text = item
            noun = ""
            verbToBeExcludes.append(item)
            info['text'] = text
            info['index'] = index
            info['english'] = possess['english']
            info['type'] = "possess_2"
            statments_and_questions_verb_to_be.append(info)
        elif item in indications:
            info = {}
            indicator = tigrina_indicators(item)
            text = item
            noun = ""
            verbToBeExcludes.append(item)
            info['text'] = text
            info['index'] = index
            info['type'] = 'indicators'
            info['english'] = indicator['english']
            if t_sentence_array[index + 1] is not None:
                noun = {'text': t_sentence_array[index + 1], 'index': index + 1}
            if noun != "":
                info['noun'] = noun
            statments_and_questions_verb_to_be.append(info)
        elif item in tigrina_whes:
            info = {}
            whes = whes_english(item)
            text = item
            verb = ""
            verbRelatedWhes = ['nabey', 'beyen', 'bkemey', 'bmntay', 'ናበይ', 'በየን', 'ብኸመይ', 'ብምንታይ']
            if item in verbRelatedWhes:
                if index + 1 < len(t_sentence_array) and t_sentence_array[index + 1] is not None:
                    verb = {'text': t_sentence_array[index+1], 'index': index+1}
            if verb != "":
                info['verb'] = verb
            info['type'] = "whes"
            info['text'] = text
            info['index'] = index
            info['english'] = whes['english']
            statments_and_questions_verb_to_be.append(info)
        elif item in tigrina_questions:
            is_tigrina_sentence_a_question = True
            pronoun = find_pronoun_from_verb_to_be(item, index)
            mypronoun = pronoun['english']
            verbToBe = 'did'
            noun = ""
            verb = ""
            if t_sentence_array[index-1] is not None:
                firstLetter = list(t_sentence_array[index-1])[0]
                if firstLetter in question_verb_additions_on_future:
                    verbToBe = 'will'
                if t_sentence_array[index-1] in alphabet_info['all_tigrina_verb_to_bes'] or t_sentence_array[index-1] in all_tigrina_verb_to_bes:
                    pass
                else:
                    if t_sentence_array[index-1] not in t_sentence_excludes:
                        verb = {'text': t_sentence_array[index-1], 'index': t_sentence_array.index(t_sentence_array[index-1])}
            isTherePastVerbToBe = any(r in tigrina_past_verb_to_be for r in t_sentence_array)
            if isTherePastVerbToBe:
                verbToBe = 'did'
            for key in t_sentence_array:
                for key2 in tigrina_verb_to_be_with_verb:
                    if t_sentence_array[key] == tigrina_verb_to_be_with_verb[key2]:
                        if mypronoun == 'he' or mypronoun == 'she':
                            verbToBe = 'is'
                        elif mypronoun == 'i':
                            verbToBe = 'am'
                        else:
                            verbToBe = 'are'
            for key in t_sentence_array:
                for key2 in tigrina_modal_verb_to_be:
                    if t_sentence_array[key] == tigrina_modal_verb_to_be[key2]:
                        pronoun = find_pronoun_from_verb_to_be(tigrina_modal_verb_to_be[key2], index)
                        mypronoun = pronoun['english']
                        verbToBe = 'should'
            for key in t_sentence_array:
                for key2 in tigrina_modal_with_possiblity_negative:
                    if t_sentence_array[key] == tigrina_modal_with_possiblity_negative[key2]:
                        verbToBe = 'can'
            for key in t_sentence_array:
                for key2 in tigrina_modal_pastVerb_to_be_negative:
                    if t_sentence_array[key] == tigrina_modal_pastVerb_to_be_negative[key2]:
                        pronoun = find_pronoun_from_verb_to_be(tigrina_modal_pastVerb_to_be_negative[key2], index)
                        mypronoun = pronoun['english']
                        verbToBe = 'should have'
            for key in t_sentence_array:
                for key2 in tigrina_modal_with_possiblity_mikone:
                    if t_sentence_array[key] == tigrina_modal_with_possiblity_mikone[key2]:
                        pronoun = find_pronoun_from_verb_to_be(tigrina_modal_with_possiblity_mikone[key2], index)
                        mypronoun = pronoun['english']
                        verbToBe = 'would' + " " + mypronoun + " " + "be"
            verbtobeInfo['pronoun'] = mypronoun
            verbtobeInfo['verbToBe'] = verbToBe
            verbtobeInfo['text'] = item
            verbtobeInfo['index'] = index
            verbtobeInfo['type'] = 'question'
            if noun != "":
                verbtobeInfo['noun'] = noun
            if verb != "":
                verbtobeInfo['verb'] = verb
            statments_and_questions_verb_to_be.append(verbtobeInfo)
        elif item in tigrina_modal_will_have or item in tigrina_modal_will_not_have:
                pronoun = find_pronoun_from_verb_to_be(item, index)
                mypronoun = pronoun['english']
                verbToBe = ""
                noun = ""
                verb = ""
                text = item
                if is_tigrina_sentence_a_question == True:
                    verbToBe = "will" + " " + mypronoun + " " + "have"
                else:
                    if item in tigrina_modal_will_not_have:
                        verbToBe = "will not have"
                        if t_sentence_array[index - 1] is not None:
                            noun = {"text": t_sentence_array[index - 1], "index": index - 1}
                    else:
                        verbToBe = "will have"
                        if t_sentence_array[index - 1] is not None:
                            noun = {"text": t_sentence_array[index - 1], "index": index - 1}
                        if t_sentence_array[index + 1] is not None:
                            if t_sentence_array[index + 1] in tigrina_none_verb_to_be:
                                verbToBeExcludes.append(t_sentence_array[index + 1])
                                text = item + " " + t_sentence_array[index + 1]
                            elif t_sentence_array[index + 1] in tigrina_modal_with_possiblity_negative:
                                verbToBe = "can have"
                                verbToBeExcludes.append(t_sentence_array[index + 1])
                                if t_sentence_array[index + 2] in tigrina_modal_with_possiblity_yikewin:
                                    verbToBe = "may have"
                                    text = item + " " + t_sentence_array[index + 1] + " " + t_sentence_array[index + 2]
                                    verbToBeExcludes.append(t_sentence_array[index + 2])
                                if t_sentence_array[index + 3] is not None:
                                    verbToBeExcludes.append(t_sentence_array[index + 3])
                                    text = item + " " + t_sentence_array[index + 1] + " " + t_sentence_array[index + 2] + " " + t_sentence_array[index + 3]
                verbtobeInfo["text"] = text
                verbtobeInfo["verbToBe"] = verbToBe
                verbtobeInfo["type"] = "verbToBe"
                verbtobeInfo["index"] = index
                if noun != "":
                    verbtobeInfo["noun"] = noun
                elif verb != "":
                    verbtobeInfo["verb"] = verb
                statments_and_questions_verb_to_be.append(verbtobeInfo)
        elif item in tigrina_modal_verb_to_be or item in tigrina_modal_verb_to_be_negative:
            pronoun = find_pronoun_from_verb_to_be(item, index)
            mypronoun = pronoun['english']
            verbToBe = ""
            noun = ""
            verb = ""
            text = item
            if t_sentence_array[index - 1] is not None:
                if t_sentence_array[index - 1] in alphabet_info.all_tigrina_verb_to_bes:
                    if is_tigrina_sentence_a_question == True:
                        if mypronoun == 'he' or mypronoun == 'she':
                            verbToBe = "does" + " " + mypronoun + " " + "have"
                        else:
                            verbToBe = "do" + " " + mypronoun + " " + "have"
                else:
                    word = t_sentence_array[index - 1]
                    firstLetter = word[0]
                    if firstLetter == 'k' or firstLetter == 'ክ':
                        if pronoun.english == 'he' or pronoun.english == 'she':
                            verbToBe = "has to"
                        else:
                            verbToBe = "have to"
                        verb = {"text": t_sentence_array[index - 1], "index": index - 1}
                    else:
                        word = t_sentence_array[index - 1]
                        if word[-1] == 'ን':
                            if pronoun.english == 'she':
                                pronoun.english = 'they'
                                mypronoun = 'they'
                        if pronoun.english == 'he' or pronoun.english == 'she':
                            verbToBe = "has"
                        else:
                            verbToBe = "have"
                        noun = {"text": t_sentence_array[index - 1], "index": index - 1}
            if item in tigrina_modal_verb_to_be_negative:
                if t_sentence_array[index - 1] is not None:
                    word = t_sentence_array[index - 1]
                    firstLetter = word[0]
                    if pronoun.english == 'he' or pronoun.english == 'she':
                        if firstLetter == 'k' or firstLetter == 'ክ':
                            verbToBe = "has not to"
                            verb = {"text": t_sentence_array[index - 1], "index": index - 1}
                        else:
                            verbToBe = "has not"
                            noun = {"text": t_sentence_array[index - 1], "index": index - 1}
                    else:
                        if firstLetter == 'k' or firstLetter == 'ክ':
                            verbToBe = "have not to"
                            verb = {"text": t_sentence_array[index - 1], "index": index - 1}
                        else:
                            verbToBe = "have not"
                            noun = {"text": t_sentence_array[index - 1], "index": index - 1}
            verbtobeInfo["text"] = text
            verbtobeInfo["verbToBe"] = verbToBe
            verbtobeInfo["pronoun"] = mypronoun
            verbtobeInfo["index"] = index
            verbtobeInfo["type"] = "verbToBe"
            if noun != "":
                verbtobeInfo["noun"] = noun
            elif verb != "":
                verbtobeInfo["verb"] = verb
            statments_and_questions_verb_to_be.append(verbtobeInfo)
        elif item in tigrina_modal_pastVerb_to_be_negative or item in tigrinaModalPastVerbToBeNegative:
            pronoun = find_pronoun_from_verb_to_be(item, index)
            mypronoun = pronoun['english']
            verbToBe = ""
            noun = ""
            verb = ""
            text = item
            if is_tigrina_sentence_a_question == True:
                verbToBe = 'had'
            else:
                verbToBe = 'had to'
            if t_sentence_array[index - 1] is not None:
                if t_sentence_array[index - 1] in alphabet_info.all_tigrina_verb_to_bes:
                    if is_tigrina_sentence_a_question == True:
                        firstLetter = t_sentence_array[index - 1][0]
                        secondLetter = t_sentence_array[index - 1][1]
                        combination = firstLetter + secondLetter
                        if firstLetter in common_first_letters_on_modal or firstLetter in common_first_letters_on_modal_past or firstLetter in common_first_letters_on_while or combination in negative_starts:
                            verbToBe = "did" + " " + mypronoun + " " + "have"
                        else:
                            verbToBe = "were" + " " + mypronoun
                    else:
                        verb = {'text': t_sentence_array[index - 1], 'index': index - 1}
                else:
                    verb = {'text': t_sentence_array[index - 1], 'index': index - 1}
            if item in tigrinaModalPastVerbToBeNegative:
                verbToBe = 'should not'
            verbtobeInfo.text = text
            if noun != "":
                verbtobeInfo.noun = noun
            elif verb != "":
                verbtobeInfo.verb = verb
            verbtobeInfo.pronoun = mypronoun
            verbtobeInfo.verbToBe = verbToBe
            verbtobeInfo.index = index
            verbtobeInfo.type = "verbToBe"
            statments_and_questions_verb_to_be.append(verbtobeInfo)
        elif item in tigrina_modal_with_possiblity_negative or item in tigrinaModalWithPossiblityNegative:
            pronoun = find_pronoun_from_verb_to_be(item, index)
            mypronoun = pronoun['english']
            verbToBe = ""
            noun = ""
            verb = ""
            text = item
            verbToBe = 'can'
            if t_sentence_array[index - 1] is not None:
                verb = {'text': t_sentence_array[index - 1], 'index': index - 1}
            if t_sentence_array[index + 1] is not None:
                if t_sentence_array[index + 1] in tigrina_none_verb_to_be:
                    pronoun = find_pronoun_from_verb_to_be(t_sentence_array[index + 1], index)
                    mypronoun = pronoun['english']
                    text = item + " " + t_sentence_array[index + 1]
                elif t_sentence_array[index + 1] in tigrina_past_verb_to_be:
                    verbToBe = "could have"
            if item in tigrinaModalWithPossiblityNegative:
                verbToBe = 'can not'
                if t_sentence_array[index + 1] is not None:
                    if t_sentence_array[index + 1] in tigrina_past_verb_to_be:
                        verbToBe = "could not have"
            verbtobeInfo.text = text
            if noun != "":
                verbtobeInfo.noun = noun
            elif verb != "":
                verbtobeInfo.verb = verb
            verbToBeExcludes.append(item)
            verbtobeInfo.verbToBe = verbToBe
            verbtobeInfo.pronoun = mypronoun
            verbtobeInfo.index = index
            verbtobeInfo.type = "verbToBe"
            statments_and_questions_verb_to_be.append(verbtobeInfo)
        elif item in tigrina_modal_with_possiblity_yikewin or item in tigrina_modal_with_possiblity_yikewin_negative:
            pronoun = find_pronoun_from_verb_to_be(item, index)
            mypronoun = pronoun['english']
            verbToBe = ""
            noun = ""
            verb = ""
            text = item
            verbToBe = 'may'
            if t_sentence_array[index - 1] is not None:
                verb = {'text': t_sentence_array[index - 1], 'index': index - 1}
            if t_sentence_array[index + 1] is not None:
                if t_sentence_array[index + 1] in tigrina_none_verb_to_be:
                    text = item + " " + t_sentence_array[index + 1]
                    pronoun = find_pronoun_from_verb_to_be(t_sentence_array[index + 1], index)
                    mypronoun = pronoun['english']
                    verbToBeExcludes.append(t_sentence_array[index + 1])
                elif t_sentence_array[index + 1] in tigrina_past_verb_to_be:
                    verbToBe = "could have"
            if t_sentence_array[index - 1] is not None:
                if t_sentence_array[index - 1] in tigrina_none_verb_to_be:
                    text = t_sentence_array[index - 1] + " " + item
                    pronoun = find_pronoun_from_verb_to_be(t_sentence_array[index - 1], index)
                    mypronoun = pronoun['english']
                    if t_sentence_array[index - 2] is not None:
                        verb = {'text': t_sentence_array[index - 2], 'index': index - 2}
                    verbToBeExcludes.append(t_sentence_array[index - 1])
            if item in tigrina_modal_with_possiblity_yikewin_negative:
                verbToBe = 'may not'
            verbtobeInfo.text = text
            verbtobeInfo.pronoun = mypronoun
            if noun != "":
                verbtobeInfo.noun = noun
            elif verb != "":
                verbtobeInfo.verb = verb
            verbtobeInfo.verbToBe = verbToBe
            verbtobeInfo.index = index
            verbtobeInfo.type = "verbToBe"
            statments_and_questions_verb_to_be.append(verbtobeInfo)
        elif item in tigrina_modal_with_possiblity_mikan or item in tigrina_modal_with_possiblity_mikan_negative:
            pronoun = find_pronoun_from_verb_to_be(item, index)
            mypronoun = pronoun['english']
            verbToBe = ""
            noun = ""
            verb = ""
            text = item
            verbToBe = 'will be'
            if t_sentence_array[index - 1] is not None:
                verb = {'text': t_sentence_array[index - 1], 'index': index - 1}
            if t_sentence_array[index + 1] is not None:
                if t_sentence_array[index + 1] in tigrina_none_verb_to_be:
                    text = item + " " + t_sentence_array[index + 1]
                    verbToBeExcludes.append(t_sentence_array[index + 1])
            if item in tigrina_modal_with_possiblity_mikan_negative:
                verbToBe = 'will not be'
            verbtobeInfo['text'] = text
            verbtobeInfo['pronoun'] = mypronoun
            if noun != "":
                verbtobeInfo['noun'] = noun
            elif verb != "":
                verbtobeInfo['verb'] = verb
            verbtobeInfo['verbToBe'] = verbToBe
            verbtobeInfo['index'] = index
            verbtobeInfo['type'] = 'verbToBe'
            statments_and_questions_verb_to_be.append(verbtobeInfo)
        elif item in tigrina_modal_with_possiblity_mikone or item in tigrina_modal_with_possiblity_mikone_negative:
            pronoun = find_pronoun_from_verb_to_be(item, index)
            mypronoun = pronoun['english']
            verbToBe = ""
            noun = ""
            verb = ""
            text = item
            verbToBe = 'would be'
            if t_sentence_array[index - 1] is not None:
                verb = {'text': t_sentence_array[index - 1], 'index': index - 1}
            if t_sentence_array[index + 1] is not None:
                if t_sentence_array[index + 1] in tigrina_none_verb_to_be:
                    text = item + " " + t_sentence_array[index + 1]
                    verbToBeExcludes.append(t_sentence_array[index + 1])
            if item in tigrina_modal_with_possiblity_mikone_negative:
                verbToBe = 'would not be'
            verbtobeInfo['text'] = text
            verbtobeInfo['pronoun'] = mypronoun
            if noun != "":
                verbtobeInfo['noun'] = noun
            elif verb != "":
                verbtobeInfo['verb'] = verb
            verbtobeInfo['verbToBe'] = verbToBe
            verbtobeInfo['index'] = index
            verbtobeInfo['type'] = 'verbToBe'
            statments_and_questions_verb_to_be.append(verbtobeInfo)
        elif item in tigrina_modal_with_possiblity_kikiel:
            pronoun = find_pronoun_from_verb_to_be(item, index)
            mypronoun = pronoun['english']
            verbToBe = ""
            noun = ""
            verb = ""
            text = item
            verbToBe = 'must'
            if t_sentence_array[index - 1] is not None:
                verb = {'text': t_sentence_array[index - 1], 'index': index - 1}
            if t_sentence_array[index + 1] is not None:
                if t_sentence_array[index + 1] in tigrina_none_verb_to_be:
                    text = item + " " + t_sentence_array[index + 1]
                    verbToBeExcludes.append(t_sentence_array[index + 1])
                if t_sentence_array[index + 1] in tigrina_modal_verb_to_be:
                    text = item + " " + t_sentence_array[index + 1]
                    verbToBeExcludes.append(t_sentence_array[index + 1])
                    pronoun = find_pronoun_from_verb_to_be(t_sentence_array[index + 1], index)
                    mypronoun = pronoun['english']
            verbtobeInfo['text'] = text
            verbtobeInfo['pronoun'] = mypronoun
            if noun != "":
                verbtobeInfo['noun'] = noun
            elif verb != "":
                verbtobeInfo['verb'] = verb
            verbtobeInfo['verbToBe'] = verbToBe
            verbtobeInfo['index'] = index
            verbtobeInfo['type'] = 'verbToBe'
            statments_and_questions_verb_to_be.append(verbtobeInfo)
        elif item in tigrina_modal_verb_to_be_negative:
            pronoun = find_pronoun_from_verb_to_be(item, index)
            mypronoun = pronoun['english']
            verbToBe = "must not"
            noun = ""
            verb = ""
            text = item

            if t_sentence_array[index-1] is not None:
                verb = {"text": t_sentence_array[index-1], "index": index-1}

            if index + 1 < len(t_sentence_array) and t_sentence_array[index + 1] is not None:
                if t_sentence_array[index+1] in tigrina_none_verb_to_be:
                    text = item + " " + t_sentence_array[index+1]
                    verbToBeExcludes.append(t_sentence_array[index+1])

            verbtobeInfo["text"] = text
            verbtobeInfo["pronoun"] = mypronoun

            if noun != "":
                verbtobeInfo["noun"] = noun
            elif verb != "":
                verbtobeInfo["verb"] = verb

            verbtobeInfo["verbToBe"] = verbToBe
            verbtobeInfo["index"] = index
            verbtobeInfo["type"] = "verbToBe"
            statments_and_questions_verb_to_be.append(verbtobeInfo)

        elif item in tigrina_verb_to_be_with_verb:
            pronoun = find_pronoun_from_verb_to_be(item, index)
            mypronoun = pronoun['english']
            verbToBe = ""
            noun = ""
            verb = ""
            text = item

            if mypronoun == 'he' or mypronoun == 'she':
                verbToBe = 'is'
            elif mypronoun == 'i':
                verbToBe = 'am'
            else:
                verbToBe = 'are'

            if t_sentence_array[index-1] is not None:
                firstLetter = t_sentence_array[index-1][0]
                secondLetter = t_sentence_array[index-1][1]
                thirdLetter = t_sentence_array[index-1][2]
                combination1 = firstLetter + secondLetter
                combination2 = combination1 + thirdLetter

                if firstLetter in common_first_letters_on_modal or combination1 in common_first_letters_on_modal or combination2 in common_first_letters_on_modal:
                    verb = {"text": t_sentence_array[index-1], "index": index-1}

                    if combination1 in negative_starts:
                        if mypronoun == 'he' or mypronoun == 'she':
                            verbToBe = 'is not'
                        elif mypronoun == 'i':
                            verbToBe = 'am not'
                        else:
                            verbToBe = 'are not'

            if index + 1 < len(t_sentence_array) and t_sentence_array[index + 1] is not None:
                if t_sentence_array[index+1] in tigrina_none_verb_to_be:
                    text = item + " " + t_sentence_array[index+1]

            verbtobeInfo["text"] = text
            verbtobeInfo["pronoun"] = mypronoun

            if noun != "":
                verbtobeInfo["noun"] = noun
            elif verb != "":
                verbtobeInfo["verb"] = verb

            verbtobeInfo["verbToBe"] = verbToBe
            verbtobeInfo["index"] = index
            verbtobeInfo["type"] = "verbToBe"
            statments_and_questions_verb_to_be.append(verbtobeInfo)
        elif item in tigrina_with_whes_present:
            pronoun = find_pronoun_from_verb_to_be(item, index)
            mypronoun = pronoun['english']
            noun = ""
            verb = ""
            text = item
            verbToBe = 'who ' + mypronoun + ' are'
            if mypronoun == 'he' or mypronoun == 'she' or mypronoun == 'i':
                verbToBe = 'who ' + mypronoun + ' is'
            type = "whesPresent"
            if t_sentence_array[index - 1] is not None:
                if t_sentence_array[index - 1] in tigrina_none_verb_to_be:
                    text = t_sentence_array[index - 1] + " " + item
                    if t_sentence_array[index - 2] is not None:
                        firstLetter = t_sentence_array[index - 2][0]
                        secondLetter = t_sentence_array[index - 2][1]
                        thirdLetter = t_sentence_array[index - 2][2]
                        combination1 = firstLetter + secondLetter
                        combination2 = combination1 + thirdLetter
                        if firstLetter in commonFirstLettersOnModal or combination1 in common_first_letters_on_modal or combination2 in common_first_letters_on_modal:
                            verb = {'text': t_sentence_array[index - 2], 'index': index - 1}
                            if combination1 in negative_starts:
                                if mypronoun == 'he' or mypronoun == 'she':
                                    verbToBe = 'is not'
                                elif mypronoun == 'i':
                                    verbToBe = 'am not'
                                else:
                                    verbToBe = 'are not'
                else:
                    firstLetter = t_sentence_array[index - 1][0]
                    secondLetter = t_sentence_array[index - 1][1]
                    thirdLetter = t_sentence_array[index - 1][2]
                    combination1 = firstLetter + secondLetter
                    combination2 = combination1 + thirdLetter
                    if firstLetter in commonFirstLettersOnModal or combination1 in common_first_letters_on_modal or combination2 in common_first_letters_on_modal:
                        verb = {'text': t_sentence_array[index - 1], 'index': index - 1}
                        if combination1 in negative_starts:
                            if mypronoun == 'he' or mypronoun == 'she':
                                verbToBe = 'is not'
                            elif mypronoun == 'i':
                                verbToBe = 'am not'
                            else:
                                verbToBe = 'are not'
            if t_sentence_array[index + 1] is not None:
                if t_sentence_array[index + 1] in tigrina_none_verb_to_be:
                    text = item + " " + t_sentence_array[index + 1]
                    verbToBeExcludes.append(t_sentence_array[index + 1])
            verbtobeInfo['text'] = text
            verbtobeInfo['pronoun'] = mypronoun
            if noun != "":
                verbtobeInfo['noun'] = noun
            elif verb != "":
                verbtobeInfo['verb'] = verb
            verbtobeInfo['verbToBe'] = verbToBe
            verbtobeInfo['index'] = index
            verbtobeInfo['type'] = "verbToBe"
            statments_and_questions_verb_to_be.append(verbtobeInfo)
        elif item in tigrina_etiWith_whes:
            pronoun = find_pronoun_from_verb_to_be(item, index)
            mypronoun = pronoun['english']
            verbToBe = 'while ' + mypronoun + ' are'
            noun = ""
            verb = ""
            text = item
            if mypronoun == 'he' or mypronoun == 'she':
                verbToBe = 'while ' + mypronoun + ' is'
            elif pronoun.english == 'i':
                verbToBe = 'while ' + mypronoun + ' am'
            if t_sentence_array[index - 1] is not None:
                if t_sentence_array[index - 1][0] != 'ክ' or t_sentence_array[index - 1][0] != 'k':
                    if mypronoun == 'he' or mypronoun == 'she' or mypronoun == 'i':
                        verbToBe = 'while ' + mypronoun + ' ' + 'was'
                    else:
                        verbToBe = 'while ' + mypronoun + ' ' + 'were'
                verb = {'text': t_sentence_array[index - 1], 'index': index - 1}
            if noun != "":
                verbtobeInfo['noun'] = noun
            elif verb != "":
                verbtobeInfo['verb'] = verb
            verbtobeInfo['verbToBe'] = verbToBe
            verbtobeInfo['text'] = text
            verbtobeInfo['index'] = index
            verbtobeInfo['pronoun'] = mypronoun
            verbtobeInfo['verb'] = verb
            verbtobeInfo['type'] = "verbToBe"
            statments_and_questions_verb_to_be.append(verbtobeInfo)
        elif item in tigrina_with_whes_past:
            pronoun = find_pronoun_from_verb_to_be(item, index)
            mypronoun = pronoun['english']
            noun = ""
            verb = ""
            text = item
            verbToBe = 'who ' + mypronoun + " were"
            if mypronoun == 'he' or mypronoun == 'she' or mypronoun == 'i':
                verbToBe = 'who ' + mypronoun + " was"
            type = "whesPast"
            if index - 1 < len(t_sentence_array):
                if t_sentence_array[index - 1] is not None:
                    if tigrina_none_verb_to_be.includes(t_sentence_array[index - 1]):
                        if t_sentence_array[index - 2] is not None:
                            verb = {'text': t_sentence_array[index - 2], 'index': t_sentence_array.index(t_sentence_array[index - 2])}
                    else:
                        verb = {'text': t_sentence_array[index - 1], 'index': t_sentence_array.index(t_sentence_array[index - 1])}
            verbtobeInfo['type'] = type
            verbtobeInfo['text'] = text
            verbtobeInfo['pronoun'] = mypronoun
            verbtobeInfo['verbToBe'] = verbToBe
            verbtobeInfo['type'] = "verbToBe"
            verbtobeInfo['index'] = index
            if noun != "":
                verbtobeInfo['noun'] = noun
            elif verb != "":
                verbtobeInfo['verb'] = verb
            statments_and_questions_verb_to_be.append(verbtobeInfo)
        elif item in tigrina_modal_with_possiblity2 or item in tigrina_modal_with_possiblity2_negative:
            pronoun = find_pronoun_from_verb_to_be(item, index)
            mypronoun = pronoun['english']
            verbToBe = ""
            noun = ""
            verb = ""
            text = item
            verbToBe = 'could'
            if index - 1 < len(t_sentence_array):
                verb = {'text': t_sentence_array[index - 1], 'index': index - 1}
            if index + 1 < len(t_sentence_array):
                if tigrina_past_verb_to_be.includes(t_sentence_array[index + 1]):
                    text = item + " " + t_sentence_array[index + 1]
                    verbToBeExcludes.append(t_sentence_array[index + 1])
            if item in tigrina_modal_with_possiblity2_negative:
                verbToBe = 'could not'
            verbtobeInfo['text'] = text
            verbtobeInfo['pronoun'] = mypronoun
            if noun != "":
                verbtobeInfo['noun'] = noun
            elif verb != "":
                verbtobeInfo['verb'] = verb
            verbtobeInfo['verbToBe'] = verbToBe
            verbtobeInfo['index'] = index
            verbtobeInfo['type'] = "verbToBe"
            statments_and_questions_verb_to_be.append(verbtobeInfo)
        elif item in tigrina_past_verb_to_be or item in tigrina_past_verb_to_be_negative:
            pronoun = find_pronoun_from_verb_to_be(item, index)
            mypronoun = pronoun['english']
            verbToBe = ""
            noun = ""
            verb = ""
            text = item
            verbToBe = 'would'
            if index - 1 < len(t_sentence_array):
                if is_tigrina_sentence_a_question == True:
                    if mypronoun == 'he' or mypronoun == 'she' or mypronoun == 'i':
                        verbToBe = 'was'
                    else:
                        verbToBe = 'were'
                else:
                    if tigrina_none_verb_to_be.includes(t_sentence_array[index - 1]):
                        if mypronoun == 'he' or mypronoun == 'she' or mypronoun == 'i':
                            verbToBe = 'was'
                        else:
                            verbToBe = 'were'
                    else:
                        if t_sentence_array[index - 1] is not None:
                            firstLetter = t_sentence_array[index - 1][0]
                            if firstLetter == 'm' or firstLetter == 'ም':
                                verbToBe = 'would  be'
                            elif firstLetter == 'y' or firstLetter == 'ይ' or firstLetter == 'የ' or firstLetter == 'ተ' or firstLetter == 'ነ':
                                if mypronoun == 'he' or mypronoun == 'she' or mypronoun == 'i':
                                    verbToBe = 'was'
                                else:
                                    verbToBe = 'were'
                            verb = {'text': t_sentence_array[index - 1], 'index': index - 1}
            if item in tigrina_modal_with_possiblity_mikan_negative:
                verbToBe = 'would not be'
            if item in tigrina_past_verb_to_be_negative:
                pronoun = find_pronoun_from_verb_to_be(item, index)
                mypronoun = pronoun['english']
                if mypronoun == 'he' or mypronoun == 'she' or mypronoun == 'i':
                    verbToBe = 'was not'
                else:
                    verbToBe = 'were not'
            verbtobeInfo['text'] = text
            verbtobeInfo['pronoun'] = mypronoun
            if noun != "":
                verbtobeInfo['noun'] = noun
            elif verb != "":
                verbtobeInfo['verb'] = verb
            verbtobeInfo['verbToBe'] = verbToBe
            verbtobeInfo['index'] = index
            verbtobeInfo['type'] = "verbToBe"
            statments_and_questions_verb_to_be.append(verbtobeInfo)
        elif item in tigrina_none_verb_to_be:
            donotWorkOnThis = False
            if index + 1 < len(t_sentence_array) and t_sentence_array[index + 1] is not None:
                if t_sentence_array[index+1] in tigrina_past_verb_to_be or t_sentence_array[index+1] in tigrina_with_whes_present:
                    donotWorkOnThis = True
            if not donotWorkOnThis:
                pronoun = find_pronoun_from_verb_to_be(item, index)
                mypronoun = pronoun['english']
                verbToBe = ""
                noun = ""
                verb = ""
                text = item
                verbToBe = 'will'
                if t_sentence_array[index-1] is not None:
                    if t_sentence_array[index-1] not in alphabet_info.all_tigrina_verb_to_bes:
                        firstLetter = t_sentence_array[index-1][0]
                        secondLetter = t_sentence_array[index-1][1]
                        thirdLetter = t_sentence_array[index-1][2]
                        combination1 = firstLetter + secondLetter
                        combination2 = combination1 + thirdLetter
                        
                        if firstLetter in common_first_letters_on_modal or combination1 in common_first_letters_on_modal or combination2 in common_first_letters_on_modal:
                            verb = {'text': t_sentence_array[index-1], 'index': index-1}
                            if combination1 in negative_starts:
                                verbToBe = 'will not'
                        else:
                            if mypronoun == 'he' or mypronoun == 'she':
                                verbToBe = 'is'
                            elif mypronoun == 'i':
                                verbToBe = 'am'
                            else:
                                verbToBe = 'are'
                            
                    if t_sentence_array[index-1] in tigrina_whes:
                        if mypronoun == 'he' or mypronoun == 'she':
                            verbToBe = 'is'
                        elif mypronoun == 'i':
                            verbToBe = 'am'
                        else:
                            verbToBe = 'are'
                
                if index + 1 < len(t_sentence_array) and t_sentence_array[index + 1] is not None:
                    if t_sentence_array[index+1] not in alphabet_info.all_tigrina_verb_to_bes:
                        firstLetter = t_sentence_array[index+1][0]
                        secondLetter = t_sentence_array[index+1][1]
                        thirdLetter = t_sentence_array[index+1][2]
                        combination1 = firstLetter + secondLetter
                        combination2 = combination1 + thirdLetter
                        
                        if firstLetter in common_first_letters_on_modal or combination1 in common_first_letters_on_modal or combination2 in common_first_letters_on_modal:
                            verb = {'text': t_sentence_array[index+1], 'index': index+1}
                            if combination1 in negative_starts:
                                verbToBe = 'will not'
                            else:
                                verbToBe = "will"
                        else:
                            if mypronoun == 'he' or mypronoun == 'she':
                                verbToBe = 'is'
                            elif mypronoun == 'i':
                                verbToBe = 'am'
                            else:
                                verbToBe = 'are'
                            
                    if t_sentence_array[index+1] in tigrinaPastVerbToBe:
                        if mypronoun == 'he' or mypronoun == 'she' or mypronoun == 'i':
                            verbToBe = 'was'
                        else:
                            verbToBe = 'were'
                            
                    if t_sentence_array[index+1] in tigrina_none_verb_to_be:
                        text = item + " " + t_sentence_array[index+1]
                    else:
                        if t_sentence_array[index+1][0] == 'ት' or t_sentence_array[index+1][0] == 'ክ' or t_sentence_array[index+1][0] == 'ን':
                            pass
                        else:
                            verbToBe = 'did'
                
                verbtobeInfo['text'] = text
                verbtobeInfo['pronoun'] = mypronoun
                if noun != "":
                    verbtobeInfo['noun'] = noun
                elif verb != "":
                    verbtobeInfo['verb'] = verb
                verbtobeInfo['verbToBe'] = verbToBe
                verbtobeInfo['index'] = index
                verbtobeInfo['type'] = "verbToBe"
                statments_and_questions_verb_to_be.append(verbtobeInfo)
        elif item in tigrina_have2 or item in tigrina_have2_past:
            pronoun = find_pronoun_from_verb_to_be(item, index)
            mypronoun = pronoun['english']
            verbToBe = ""
            noun = ""
            verb = ""
            text = item
            verbToBe = "have"
            if item in tigrina_have2_past:
                verbToBe = "had"
            else:
                if mypronoun == 'he' or mypronoun == 'she':
                    verbToBe = "has"
            
            if noun != "":
                verbtobeInfo.noun = noun
            elif verb != "":
                verbtobeInfo.verb = verb
            
            verbtobeInfo.text = text
            verbtobeInfo.index = index
            verbtobeInfo.pronoun = mypronoun
            verbtobeInfo.verbToBe = verbToBe
            verbtobeInfo.type = "verbToBe"
            statments_and_questions_verb_to_be.append(verbtobeInfo)
        
        elif item in tigrina_verb_to_be_xenhe or item in tigrina_verb_to_be_xenhe_negative:
            pronoun = find_pronoun_from_verb_to_be(item, index)
            verbToBe = ""
            noun = ""
            verb = ""
            text = item
            verbToBe = "have"
            
            if is_tigrina_sentence_a_question == True:
                verbToBe = "have"
                mypronoun = pronoun['english'] + " been"
            else:
                verbToBe = "have been"
                mypronoun = pronoun['english']
            
            if mypronoun == 'he' or mypronoun == 'she':
                verbToBe = 'has'
            
            if item in tigrina_verb_to_be_xenhe_negative:
                verbToBe = "have not"
                if mypronoun == 'he' or mypronoun == 'she':
                    verbToBe = 'has not'
            
            if noun != "":
                verbtobeInfo.noun = noun
            elif verb != "":
                verbtobeInfo.verb = verb
            
            verbtobeInfo.text = text
            verbtobeInfo.index = index
            verbtobeInfo.pronoun = mypronoun
            verbtobeInfo.verbToBe = verbToBe
            verbtobeInfo.type = "verbToBe"
            statments_and_questions_verb_to_be.append(verbtobeInfo)
        elif item in tigrina_verb_to_be_history:
            pronoun = find_pronoun_from_verb_to_be(item, index)
            mypronoun = pronoun['english']
            verbToBe = ""
            noun = ""
            verb = ""
            text = item
            verbToBe = "were"
            if mypronoun == 'he' or mypronoun == 'she':
                verbToBe = 'was'
            if noun != "":
                verbtobeInfo.noun = noun
            elif verb != "":
                verbtobeInfo.verb = verb
            verbtobeInfo.text = text
            verbtobeInfo.index = index
            verbtobeInfo.pronoun = mypronoun
            verbtobeInfo.verbToBe = verbToBe
            verbtobeInfo.type = "verbToBe"
            statments_and_questions_verb_to_be.append(verbtobeInfo)
        elif item in zeykona:
            pronoun = find_pronoun_from_verb_to_be(item, index)
            mypronoun = pronoun['english']
            verbToBe = ""
            noun = ""
            verb = ""
            text = item
            verbToBe = "are not"
            if mypronoun == 'he' or mypronoun == 'she':
                verbToBe = 'is not'
            elif mypronoun == 'i':
                verbToBe = 'am not'
            if noun != "":
                verbtobeInfo.noun = noun
            elif verb != "":
                verbtobeInfo.verb = verb
            verbtobeInfo.text = text
            verbtobeInfo.pronoun = mypronoun
            verbtobeInfo.verbToBe = verbToBe
            verbtobeInfo.index = index
            verbtobeInfo.type = "verbToBe"
            statments_and_questions_verb_to_be.append(verbtobeInfo)
        elif item in entekoyne:
            pronoun = find_pronoun_from_verb_to_be(item, index)
            mypronoun = pronoun['english']
            verbToBe = ""
            noun = ""
            verb = ""
            text = item
            verbToBe = "are"
            if mypronoun == 'he' or mypronoun == 'she':
                verbToBe = 'is not'
            elif mypronoun == 'i':
                verbToBe = 'am not'
            if noun != "":
                verbtobeInfo.noun = noun
            elif verb != "":
                verbtobeInfo.verb = verb
            verbtobeInfo.text = text
            verbtobeInfo.pronoun = "if " + mypronoun
            verbtobeInfo.verbToBe = verbToBe
            verbtobeInfo.type = "verbToBe"
            verbtobeInfo.index = index
            statments_and_questions_verb_to_be.append(verbtobeInfo)
        elif item in ente_zeykoyna:
            pronoun = find_pronoun_from_verb_to_be(item, index)
            mypronoun = pronoun['english']
            verbToBe = ""
            noun = ""
            verb = ""
            text = item
            verbToBe = "are"
            if mypronoun == 'he' or mypronoun == 'she':
                verbToBe = 'is not'
            elif mypronoun == 'i':
                verbToBe = 'am not'
            if noun != "":
                verbtobeInfo.noun = noun
            elif verb != "":
                verbtobeInfo.verb = verb
            verbtobeInfo.text = text
            verbtobeInfo.pronoun = "if " + mypronoun
            verbtobeInfo.verbToBe = verbToBe
            verbtobeInfo.type = "verbToBe"
            verbtobeInfo.index = index
            statments_and_questions_verb_to_be.append(verbtobeInfo)
        elif item in kabkone:
            pronoun = find_pronoun_from_verb_to_be(item, index)
            mypronoun = pronoun['english']
            verbToBe = ""
            noun = ""
            verb = ""
            text = item
            verbToBe = "are"
            if mypronoun == 'he' or mypronoun == 'she':
                verbToBe = 'is'
            elif mypronoun == 'i':
                verbToBe = 'am'
            if noun != "":
                verbtobeInfo.noun = noun
            elif verb != "":
                verbtobeInfo.verb = verb
            verbtobeInfo.text = text
            verbtobeInfo.pronoun = "if " + mypronoun
            verbtobeInfo.verbToBe = verbToBe
            verbtobeInfo.type = "verbToBe"
            verbtobeInfo.index = index
            statments_and_questions_verb_to_be.append(verbtobeInfo)
        elif item in zeymkona:
            pronoun = find_pronoun_from_verb_to_be(item, index)
            mypronoun = pronoun['english']
            verbToBe = ""
            text = item
            verbToBe = "for not being"
            verbtobeInfo.text = text
            verbtobeInfo.verbToBe = verbToBe
            verbtobeInfo.type = "verbToBe"
            verbtobeInfo.index = index
            statments_and_questions_verb_to_be.append(verbtobeInfo)
        elif item in koyne or item in kone:
            pronoun = find_pronoun_from_verb_to_be(item, index)
            mypronoun = pronoun['english']
            verbToBe = ""
            text = item
            verbToBe = "became"
            verbtobeInfo.text = text
            verbtobeInfo.pronoun = mypronoun
            verbtobeInfo.verbToBe = verbToBe
            verbtobeInfo.type = "verbToBe"
            verbtobeInfo.index = index
            statments_and_questions_verb_to_be.append(verbtobeInfo)
        elif item in keykone:
            pronoun = find_pronoun_from_verb_to_be(item, index)
            mypronoun = pronoun['english']
            verbToBe = ""
            text = item
            verbToBe = "never be"
            verbtobeInfo.text = text
            verbtobeInfo.pronoun = mypronoun
            verbtobeInfo.verbToBe = verbToBe
            verbtobeInfo.type = "verbToBe"
            verbtobeInfo.index = index
            statments_and_questions_verb_to_be.append(verbtobeInfo)
        elif item in zeykealku:
            pronoun = find_pronoun_from_verb_to_be(item, index)
            mypronoun = pronoun['english']
            verbToBe = ""
            text = item
            verbToBe = "could not"
            verbtobeInfo.text = text
            verbtobeInfo.pronoun = mypronoun
            verbtobeInfo.verbToBe = verbToBe
            verbtobeInfo.type = "verbToBe"
            verbtobeInfo.index = index
            statments_and_questions_verb_to_be.append(verbtobeInfo)
        elif item in kealku:
            pronoun = find_pronoun_from_verb_to_be(item, index)
            mypronoun = pronoun['english']
            verbToBe = ""
            text = item
            verbToBe = "could"
            verbtobeInfo.text = text
            verbtobeInfo.pronoun = mypronoun
            verbtobeInfo.verbToBe = verbToBe
            verbtobeInfo.type = "verbToBe"
            verbtobeInfo.index = index
            statments_and_questions_verb_to_be.append(verbtobeInfo)
        elif item in zeymkaaley:
            pronoun = find_pronoun_from_verb_to_be(item, index)
            mypronoun = pronoun['english']
            verbToBe = ""
            text = item
            verbToBe = "for unable to"
            verbtobeInfo.text = text
            verbtobeInfo.pronoun = mypronoun
            verbtobeInfo.verbToBe = verbToBe
            verbtobeInfo.type = "verbToBe"
            verbtobeInfo.index = index
            statments_and_questions_verb_to_be.append(verbtobeInfo)
        elif item in zeykiel:
            pronoun = find_pronoun_from_verb_to_be(item, index)
            mypronoun = pronoun['english']
            verbToBe = ""
            text = item
            verbToBe = "could not"
            verbtobeInfo.text = text
            verbtobeInfo.pronoun = mypronoun
            verbtobeInfo.verbToBe = verbToBe
            verbtobeInfo.type = "verbToBe"
            verbtobeInfo.index = index
            statments_and_questions_verb_to_be.append(verbtobeInfo)
        elif item in keykaale:
            isItKeykaale_2 = "no"
            if t_sentence_array[index + 1] is not None:
                if t_sentence_array[index + 1] in tigrina_etiWith_whes:
                    isItKeykaale_2 = "yes"
            if isItKeykaale_2 == 'yes':
                pronoun = find_pronoun_from_verb_to_be(item, index)
                mypronoun = pronoun['english']
                verbToBe = ""
                text = item
                verbToBe = "are not able to"
                if mypronoun == 'she' or mypronoun == 'he':
                    verbToBe = "is not able to"
                elif mypronoun == 'i':
                    verbToBe = "am not able to"
                verbtobeInfo.text = text
                verbtobeInfo.pronoun = "when " + mypronoun
                verbtobeInfo.verbToBe = verbToBe
                verbtobeInfo.type = "verbToBe"
                verbtobeInfo.index = index
                statments_and_questions_verb_to_be.append(verbtobeInfo)
            else:
                pronoun = find_pronoun_from_verb_to_be(item, index)
                mypronoun = pronoun['english']
                verbToBe = ""
                text = item
                verbToBe = "without being able to"
                verbtobeInfo.text = text
                verbtobeInfo.pronoun = mypronoun
                verbtobeInfo.verbToBe = verbToBe
                verbtobeInfo.type = "verbToBe"
                verbtobeInfo.index = index
                statments_and_questions_verb_to_be.append(verbtobeInfo)
        elif item[0] == 'ዝ':
            beforeIndexCollector = []
            afterIndexCollector = []
            for index2, item2 in enumerate(t_sentence_array):
                if index > index2:
                    beforeIndexCollector.append(item2)
                else:
                    afterIndexCollector.append(item2)
            englishPronoun = ""
            for key in beforeIndexCollector:
                englishPronoun1 = pronouns(beforeIndexCollector[key])
                if englishPronoun1.pronoun != '':
                    englishPronoun = englishPronoun1.pronoun
            verbToBe = ""
            for key in afterIndexCollector:
                verbToBeChecker = verb_to_be_pastence_or_present_checker(afterIndexCollector[key])
                if verbToBeChecker.verbToBe != '':
                    verbToBe = verbToBeChecker.verbToBe
            if verbToBe != "":
                if englishPronoun != "":
                    if englishPronoun == 'i':
                        if verbToBe == 'is':
                            verbToBe = "am"
                        else:
                            verbToBe = "was"
                    elif englishPronoun == 'she' or englishPronoun == 'he' or englishPronoun == 'it':
                        if verbToBe == 'is':
                            verbToBe = "is"
                        else:
                            verbToBe = "was"
                    elif englishPronoun == 'you' or englishPronoun == 'they' or englishPronoun == 'we':
                        if verbToBe == 'are':
                            verbToBe = "are"
                        else:
                            verbToBe = "were"
            text = item
            verbtobeInfo.text = text
            verbtobeInfo.pronoun = englishPronoun
            verbtobeInfo.verbToBe = verbToBe
            verbtobeInfo.type = "verbToBe"
            verbtobeInfo.index = index
            statments_and_questions_verb_to_be.append(verbtobeInfo)
        else:
            pairs_checker = ['ክት', 'ኣይ', 'ዘይ', 'ከይ', 'ምስ']
            single_checker = ['ም', 'መ', 'የ', 'ት', 'ክ', 'ይ', 'ከ', 'ን']
            def check_verb(item, index):
                verbtobeInfo = {}

                input_item = list(item)

                if len(input_item) > 1:
                    first_item = input_item[0]
                    second_item = input_item[1]
                    combination = first_item + second_item

                    if combination in pairs_checker or first_item in single_checker:
                        verbtobeInfo["verbToBe"] = "is"
                        verbtobeInfo["pronoun"] = "he"
                    else:
                        verbtobeInfo["verbToBe"] = "was"
                        verbtobeInfo["pronoun"] = "he"
                    
                    verbtobeInfo["index"] = index
                    verbtobeInfo["type"] = "verbToBe"
                    verbtobeInfo["verb"] = item

                return verbtobeInfo
            verbtobeInfo = check_verb(item, index)
            statments_and_questions_verb_to_be.append(verbtobeInfo)

    return statments_and_questions_verb_to_be


class VerbToBeInfo:
    @staticmethod
    def verb_to_be(text):
        try:
            result = fabricate(text)
            return result
        except Exception as error:
            return f"There is something wrong!, {error}"
    
    def breakers(self):
        result=tigrina_verb_to_be_with_verb
        return result
    
    def verb_to_be_trans(self):
        result=verb_to_bes_obj
        return result
verb_to_be_info = VerbToBeInfo()